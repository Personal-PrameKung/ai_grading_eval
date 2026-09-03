"""Score-agreement metrics kept independent from the evaluation framework."""

from pydantic import BaseModel


class EvaluationMetrics(BaseModel):
    case_count: int
    mae: float
    qwk: float


def mean_absolute_error(human_scores: list[int], ai_scores: list[int]) -> float:
    _validate_score_pairs(human_scores, ai_scores)
    return sum(abs(human - ai) for human, ai in zip(human_scores, ai_scores, strict=True)) / len(human_scores)


def quadratic_weighted_kappa(
    human_scores: list[int], ai_scores: list[int], *, minimum: int = 0, maximum: int | None = None
) -> float:
    """Calculate quadratic weighted Cohen's kappa for integer ordinal scores."""

    _validate_score_pairs(human_scores, ai_scores)
    maximum = max((*human_scores, *ai_scores)) if maximum is None else maximum
    if minimum > maximum:
        raise ValueError("minimum must not exceed maximum")
    if any(score < minimum or score > maximum for score in (*human_scores, *ai_scores)):
        raise ValueError("all scores must be inside the configured range")
    if minimum == maximum:
        return 1.0

    category_count = maximum - minimum + 1
    human_histogram = [0] * category_count
    ai_histogram = [0] * category_count
    observed_weighted = 0.0

    denominator = (category_count - 1) ** 2
    for human, ai in zip(human_scores, ai_scores, strict=True):
        human_index = human - minimum
        ai_index = ai - minimum
        human_histogram[human_index] += 1
        ai_histogram[ai_index] += 1
        observed_weighted += ((human_index - ai_index) ** 2) / denominator

    sample_count = len(human_scores)
    observed_weighted /= sample_count
    expected_weighted = sum(
        ((human_index - ai_index) ** 2) / denominator
        * human_histogram[human_index]
        * ai_histogram[ai_index]
        / (sample_count**2)
        for human_index in range(category_count)
        for ai_index in range(category_count)
    )

    if expected_weighted == 0:
        return 1.0 if observed_weighted == 0 else 0.0
    return 1.0 - observed_weighted / expected_weighted


def calculate_metrics(human_scores: list[int], ai_scores: list[int], *, maximum: int) -> EvaluationMetrics:
    return EvaluationMetrics(
        case_count=len(human_scores),
        mae=mean_absolute_error(human_scores, ai_scores),
        qwk=quadratic_weighted_kappa(human_scores, ai_scores, maximum=maximum),
    )


def _validate_score_pairs(human_scores: list[int], ai_scores: list[int]) -> None:
    if not human_scores:
        raise ValueError("at least one score pair is required")
    if len(human_scores) != len(ai_scores):
        raise ValueError("human_scores and ai_scores must have equal lengths")
