"""Convert AP Calculus OCR Markdown into the requested response-level dataset.

The converter is intentionally dependency-free.  It uses the stable directory
layout created by ``ocr_to_markdown.py`` and keeps uncertain OCR extraction in
an exceptions CSV instead of silently inventing values.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path


FIELDS = [
    "question_id",
    "source",
    "subject",
    "topic",
    "question_type",
    "question_text",
    "reference_answer",
    "required_points",
    "rubric",
    "max_score",
    "response_id",
    "answer_text",
    "final_answer",
    "answer_image_path",
    "human_score",
    "human_feedback",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")


def clean(text: str) -> str:
    text = re.sub(r"<!-- Page \d+ -->", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def question_parts(text: str) -> dict[int, dict[str, str]]:
    """Parse numbered questions and anchored A-D part labels."""
    matches = list(re.finditer(r"(?m)^\s*([1-6])\.\s+", text))
    result: dict[int, dict[str, str]] = {}
    for i, match in enumerate(matches):
        number = int(match.group(1))
        block = text[match.end() : matches[i + 1].start() if i + 1 < len(matches) else len(text)]
        part_matches = list(re.finditer(r"(?im)^\s*(?:[#>*-]+\s*)?(?:\*{0,2}\s*)?(?:Part\s+)?(?:([A-D])\*{0,2}\.?\s+|\(([a-d])\)\*{0,2}\.?\s+)", block))
        if not part_matches:
            continue
        stem = block[: part_matches[0].start()].strip()
        result[number] = {}
        for j, part_match in enumerate(part_matches):
            part = (part_match.group(1) or part_match.group(2)).upper()
            body = block[part_match.end() : part_matches[j + 1].start() if j + 1 < len(part_matches) else len(block)]
            result[number][part] = clean(stem + "\n\n" + body)
    return result


def extract_report_topics(report_paths: list[Path], track: str) -> dict[int, tuple[str, str]]:
    topics: dict[int, tuple[str, str]] = {}
    for path in report_paths:
        text = read(path)
        headings = list(re.finditer(r"(?m)^# Question ([^\n]+)", text))
        for i, heading in enumerate(headings):
            label = heading.group(1)
            end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
            block = text[heading.end() : end]
            # Reports sometimes combine AB1/BC1.  Prefer the requested track.
            if not re.search(rf"\b{track}\s*\d+\b", label) and f"{track}{re.search(r'\d+', label).group(0) if re.search(r'\d+', label) else ''}" not in label:
                continue
            q_match = re.search(rf"\b{track}\s*(\d+)\b", label)
            if not q_match:
                q_match = re.search(r"Question\s*(\d+)", block)
            if not q_match:
                continue
            qnum = int(q_match.group(1))
            task = re.search(r"(?m)^Task:\s*(.+)$", block)
            topic = re.search(r"(?m)^Topic:\s*(.+)$", block)
            if topic or task:
                topics.setdefault(qnum, (topic.group(1).strip() if topic else "", task.group(1).strip() if task else ""))
    return topics


def guideline_parts(text: str) -> dict[str, dict[str, object]]:
    """Extract point ids and a model-answer/rubric block for each part.

    The OCR layout varies: some scoring tables put A-D in table rows, while
    others use standalone labels.  "Scoring Notes for Part X" is the reliable
    boundary present in both layouts, so points are collected between those
    boundaries and deduplicated in reading order.
    """
    notes = list(re.finditer(r"(?im)Scoring Notes for Part\s+([A-D])", text))
    if not notes:
        totals = list(re.finditer(r"(?im)^\s*\*{0,2}\s*Total for part\s+\(?([a-d])\)?(?:\s+(\d+)\s+points)?", text))
        result: dict[str, dict[str, object]] = {}
        previous_end = 0
        for total in totals:
            part = total.group(1).upper()
            section = text[previous_end:total.end()]
            split = re.split(r"(?im)^#?\s*Scoring notes:\s*", section, maxsplit=1)
            reference = clean(split[0])
            rubric = clean(split[1]) if len(split) > 1 else ""
            score_text = total.group(2)
            if not score_text:
                lookahead = text[total.end() : total.end() + 80]
                score_match = re.search(r"(\d+)\s+points?", lookahead, flags=re.IGNORECASE)
                score_text = score_match.group(1) if score_match else ""
            max_score = int(score_text) if score_text else 0
            result[part] = {
                "points": [f"P{i}" for i in range(1, max_score + 1)],
                "reference": reference,
                "rubric": rubric,
                "max_score": max_score,
            }
            previous_end = total.end()
        return result
    result: dict[str, dict[str, object]] = {}
    assigned_points: set[str] = set()
    for i, note in enumerate(notes):
        part = note.group(1).upper()
        start = 0 if i == 0 else notes[i - 1].end()
        end = note.start()
        model = text[start:end]
        note_end = notes[i + 1].start() if i + 1 < len(notes) else len(text)
        notes_block = text[note.start():note_end]
        point_ids = []
        for point in re.findall(r"\bP(\d+)\b", model):
            value = f"P{point}"
            if value not in point_ids and value not in assigned_points:
                point_ids.append(value)
        assigned_points.update(point_ids)
        # Keep model solution before scoring notes as reference answer.
        reference = clean(re.split(r"(?im)###?\s*Scoring Notes for Part\s+[A-D]|\*\*Scoring Notes for Part\s+[A-D]\*\*", model)[0])
        rubric = clean(notes_block)
        result[part] = {
            "points": point_ids,
            "reference": reference,
            "rubric": rubric,
            "max_score": len(point_ids),
        }
    return result


def guidelines_by_question(text: str) -> dict[int, dict[str, dict[str, object]]]:
    blocks = list(re.finditer(r"(?im)^#{3,4}\s*Question\s+(\d+)\b", text))
    result: dict[int, dict[str, dict[str, object]]] = {}
    for i, match in enumerate(blocks):
        end = blocks[i + 1].start() if i + 1 < len(blocks) else len(text)
        result[int(match.group(1))] = guideline_parts(text[match.end():end])
    return result


def relative_asset_path(md_path: Path, link: str, root: Path) -> str:
    path = (md_path.parent / link).resolve()
    try:
        return path.relative_to(root.resolve()).as_posix()
    except ValueError:
        return link.replace("\\", "/")


def sample_blocks(text: str) -> dict[str, str]:
    """Return answer pages keyed by labels such as 1A, 1B, 1C."""
    matches = list(re.finditer(r"(?m)^Sample\s+(\d+[A-Z])(?:\s+\d+\s+of\s+\d+)?\s*$", text))
    blocks: dict[str, str] = {}
    for index, match in enumerate(matches):
        label = match.group(1)
        if label in blocks:
            continue
        end = len(text)
        for nxt in matches[index + 1 :]:
            if nxt.group(1) != label:
                end = nxt.start()
                break
        block = text[match.end():end]
        commentary = re.search(r"(?m)^AP CALCULUS .*SCORING COMMENTARY", block)
        if commentary:
            block = block[:commentary.start()]
        blocks[label] = block.strip()
    return blocks


def sample_parts(block: str, md_path: Path, root: Path) -> dict[str, dict[str, object]]:
    labels = list(re.finditer(
        r"(?im)^\s*(?:[#>*-]+\s*)?(?:\*{0,2}\s*)?(?:PART\s+(?:\(([a-d])\)|([A-D]))|Response\s+for\s+question\s+\d+\s*\(([a-d])\))(?:\s*\*{0,2})\s*$",
        block,
    ))
    result: dict[str, dict[str, object]] = {}
    for i, label in enumerate(labels):
        part = next((value for value in label.groups() if value), "").upper()
        end = labels[i + 1].start() if i + 1 < len(labels) else len(block)
        body = block[label.end():end]
        images = [relative_asset_path(md_path, x, root) for x in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", body)]
        body = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", body)
        body = re.sub(r"(?m)^Page\s+\d+\s*$", "", body)
        body = re.sub(r"(?m)^Q\d+(?:\s+Q\d+)*\s*$", "", body)
        body = re.sub(r"(?m)^Q\d+/\d+\s*$", "", body)
        body = re.sub(r"(?m)^\d{6,8}\s*$", "", body)
        body = re.sub(r"(?m)^Use a pencil.*$", "", body)
        body = re.sub(r"(?m)^Do NOT write.*$", "", body)
        body = clean(body)
        result[part] = {"text": body, "images": images}
    return result


def commentary_blocks(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"(?m)^\s*(?:#{1,6}\s+)?\*{0,2}\s*Sample:\s*(\d+[A-Z])\s*\*{0,2}\s*$", text))
    result = {}
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        result[match.group(1)] = text[match.end():end].strip()
    return result


def score_and_feedback(commentary: str, part: str, points: list[str]) -> tuple[str, str]:
    score_match = re.search(r"\*\*Score:\s*(\d+)\s*\(([-\d]+)\)\*\*", commentary)
    score = ""
    if score_match:
        values = [int(x) for x in score_match.group(2).split("-") if x]
        earned = values[:]
        point_indexes = {int(p[1:]) - 1 for p in points}
        score = str(sum(earned[i] for i in point_indexes if i < len(earned)))
    if not score:
        part_match = re.search(rf"(?im)(\d+)\s+points in part\s+\(?{part}\)?(?=[^a-z]|$)", commentary)
        if part_match:
            score = part_match.group(1)
    sections = list(re.finditer(r"(?mi)^\s*In part\s+\(?([A-D])\)?(?=[^a-z]|$)", commentary))
    feedback = ""
    for i, section in enumerate(sections):
        if section.group(1).upper() != part:
            continue
        end = sections[i + 1].start() if i + 1 < len(sections) else len(commentary)
        feedback = clean(commentary[section.start():end])
        break
    return score, feedback


def final_answer(text: str) -> str:
    boxed = re.findall(r"\\boxed\{([^{}]+)\}", text)
    if boxed:
        return boxed[-1].strip()
    matches = re.findall(r"(?:\bat\b|\bis\b|=)\s*([^\n$]+)", text, flags=re.IGNORECASE)
    if matches:
        candidate = matches[-1].strip().strip(".$")
        if len(candidate) < 120:
            return candidate
    lines = []
    for line in text.splitlines():
        value = line.strip()
        if not value or value.lower() in {"page", "go on to the next page"}:
            continue
        if re.fullmatch(r"Q\d+/\d+|\d{6,8}", value, flags=re.IGNORECASE):
            continue
        lines.append(value)
    return lines[-1] if lines else ""


def add_exception(exceptions: list[dict[str, str]], code: str, record: str, detail: str) -> None:
    exceptions.append({"code": code, "record": record, "detail": detail})


def convert(root: Path, output: Path) -> dict[str, int]:
    md_root = root / "ocr_markdown"
    output.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, str]] = []
    question_bank: list[dict[str, str]] = []
    exceptions: list[dict[str, str]] = []
    report_counts = defaultdict(int)

    for track_dir in sorted(p for p in md_root.iterdir() if p.is_dir()):
        track = track_dir.name
        for year_dir in sorted(p for p in track_dir.iterdir() if p.is_dir()):
            year = year_dir.name
            q_files = list((year_dir / "questions").glob("*.md"))
            if not q_files:
                continue
            questions = question_parts(read(q_files[0]))
            report_topics = extract_report_topics(list((year_dir / "reports").glob("*.md")), track)
            guideline_files = list((year_dir / "scoring_guidelines").glob("*.md"))
            guidelines = guidelines_by_question(read(guideline_files[0])) if guideline_files else {}
            sample_files = sorted((year_dir / "sample_responses").glob("*.md"))
            sample_data: dict[str, dict[str, dict[str, object]]] = {}
            comment_data: dict[str, dict[str, str]] = {}
            for sample_file in sample_files:
                q_match = re.search(r"-q(\d+)\.md$", sample_file.name)
                if not q_match:
                    continue
                qnum = q_match.group(1)
                text = read(sample_file)
                sample_data[qnum] = {label: sample_parts(block, sample_file, root) for label, block in sample_blocks(text).items()}
                comment_data[qnum] = commentary_blocks(text)
            for qnum, parts in sorted(questions.items()):
                topic, task = report_topics.get(qnum, ("", ""))
                for part, question_text in sorted(parts.items()):
                    qid = f"AP_CALCULUS_{track}_{year}_Q{qnum}_{part}"
                    guide = guidelines.get(qnum, {}).get(part, {})
                    points = guide.get("points", []) if isinstance(guide, dict) else []
                    points = list(points) if isinstance(points, list) else []
                    base = {
                        "question_id": qid,
                        "source": "AP",
                        "subject": f"Calculus {track}",
                        "topic": topic,
                        "question_type": "Free Response - Problem Solving",
                        "question_text": question_text,
                        "reference_answer": str(guide.get("reference", "")) if isinstance(guide, dict) else "",
                        "required_points": "; ".join(points),
                        "rubric": str(guide.get("rubric", "")) if isinstance(guide, dict) else "",
                        "max_score": str(guide.get("max_score", "")) if isinstance(guide, dict) else "",
                    }
                    if not guide:
                        add_exception(exceptions, "MISSING_RUBRIC", qid, f"No scoring guideline for {track} {year} Q{qnum} Part {part}")
                    labels = sorted(label for label in sample_data.get(str(qnum), {}) if label.startswith(str(qnum)))
                    if not labels:
                        question_bank.append({**base, "response_id": "", "answer_text": "", "final_answer": "", "answer_image_path": "", "human_score": "", "human_feedback": ""})
                        if sample_files:
                            add_exception(exceptions, "MISSING_SAMPLE_PART", qid, "No sample response part was parsed")
                        continue
                    for label in labels:
                        sample = sample_data[str(qnum)][label].get(part, {})
                        if not sample:
                            add_exception(exceptions, "MISSING_SAMPLE_PART", f"{qid}_{label}", "No answer text block")
                            continue
                        answer = str(sample.get("text", ""))
                        images = list(sample.get("images", []))
                        response_id = f"{qid}_{label}"
                        score, feedback = score_and_feedback(comment_data.get(str(qnum), {}).get(label, ""), part, points)
                        if not answer:
                            add_exception(exceptions, "EMPTY_ANSWER_TEXT", response_id, "OCR answer block is empty")
                        if not images:
                            add_exception(exceptions, "MISSING_IMAGE", response_id, "No image link in the sample part")
                        answer_final = final_answer(answer)
                        if not answer_final:
                            add_exception(exceptions, "AMBIGUOUS_FINAL_ANSWER", response_id, "Could not identify a final answer")
                        rows.append({**base, "response_id": response_id, "answer_text": answer, "final_answer": answer_final, "answer_image_path": "; ".join(images), "human_score": score, "human_feedback": feedback})

            report_counts[f"{track}_{year}_questions"] += len(questions)
            report_counts[f"{track}_{year}_responses"] += sum(len(v) for v in sample_data.values())

    with (output / "dataset.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    with (output / "question_bank.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(question_bank)
    with (output / "exceptions.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        writer = csv.DictWriter(fh, fieldnames=["code", "record", "detail"])
        writer.writeheader()
        writer.writerows(exceptions)
    (output / "metadata.json").write_text(json.dumps({"counts": dict(report_counts), "rows": len(rows), "question_bank_rows": len(question_bank), "exceptions": len(exceptions)}, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"rows": len(rows), "question_bank_rows": len(question_bank), "exceptions": len(exceptions)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    output = args.output or args.root / "dataset_output"
    counts = convert(args.root.resolve(), output.resolve())
    print(json.dumps(counts, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
