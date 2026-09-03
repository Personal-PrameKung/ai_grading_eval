import json
import tempfile
import unittest
from pathlib import Path

from pydantic import ValidationError

from ai_grading_eval.data import load_cases
from ai_grading_eval.grader import ExactAnswerBaseline
from ai_grading_eval.metrics import mean_absolute_error, quadratic_weighted_kappa
from ai_grading_eval.models import GraderInput, GraderOutput
from ai_grading_eval.runner import run_evaluation


ROOT = Path(__file__).parents[1]
DATASET = ROOT / "data" / "evaluation_sample.jsonl"


class DatasetTests(unittest.TestCase):
    def test_sample_dataset_is_valid_and_ids_are_unique(self) -> None:
        cases = load_cases(DATASET)
        self.assertEqual(len(cases), 8)
        self.assertEqual(len({case.response_id for case in cases}), 8)

    def test_human_labels_are_not_in_grader_input(self) -> None:
        grader_input = GraderInput.from_case(load_cases(DATASET)[0])
        self.assertNotIn("human_score", grader_input.model_dump())
        self.assertNotIn("human_feedback", grader_input.model_dump())

    def test_invalid_rubric_total_is_rejected(self) -> None:
        payload = json.loads(DATASET.read_text().splitlines()[0])
        payload["max_score"] = 3
        with self.assertRaises(ValidationError):
            from ai_grading_eval.models import EvaluationCase

            EvaluationCase.model_validate(payload)


class MetricTests(unittest.TestCase):
    def test_perfect_agreement(self) -> None:
        scores = [0, 1, 2, 2]
        self.assertEqual(mean_absolute_error(scores, scores), 0)
        self.assertEqual(quadratic_weighted_kappa(scores, scores, maximum=2), 1)

    def test_known_disagreement(self) -> None:
        human = [0, 1, 2]
        ai = [2, 1, 0]
        self.assertAlmostEqual(mean_absolute_error(human, ai), 4 / 3)
        self.assertAlmostEqual(quadratic_weighted_kappa(human, ai, maximum=2), -1)


class RunnerTests(unittest.TestCase):
    def test_baseline_run_writes_separate_results(self) -> None:
        cases = load_cases(DATASET)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "run.jsonl"
            results, metrics = run_evaluation(
                cases,
                ExactAnswerBaseline(),
                grader_version="test-v1",
                prompt_version="none",
                model="local",
                output_path=output,
                run_id="test-run",
            )
            self.assertEqual(len(results), len(cases))
            self.assertEqual(metrics.case_count, len(cases))
            self.assertEqual(len(output.read_text().splitlines()), len(cases))
            self.assertNotIn("human_score", json.loads(output.read_text().splitlines()[0]))

    def test_out_of_range_grader_score_is_rejected(self) -> None:
        class InvalidGrader:
            def grade(self, grader_input: GraderInput) -> GraderOutput:
                return GraderOutput(score=grader_input.max_score + 1, feedback="invalid")

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "exceeds max_score"):
                run_evaluation(
                    load_cases(DATASET)[:1],
                    InvalidGrader(),
                    grader_version="invalid",
                    prompt_version="none",
                    model="local",
                    output_path=Path(directory) / "run.jsonl",
                )


if __name__ == "__main__":
    unittest.main()
