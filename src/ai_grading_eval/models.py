"""Validated schemas for ground truth and experiment outputs."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, model_validator


class RubricCriterion(BaseModel):
    model_config = ConfigDict(extra="forbid")

    criterion: str = Field(min_length=1)
    score: int = Field(gt=0)


class EvaluationCase(BaseModel):
    """One immutable, human-graded evaluation example."""

    model_config = ConfigDict(extra="forbid")

    question_id: str = Field(min_length=1)
    source: str = Field(min_length=1)
    subject: str = Field(min_length=1)
    topic: str = Field(min_length=1)
    question_type: str = Field(min_length=1)
    question_text: str = Field(min_length=1)
    reference_answer: str = Field(min_length=1)
    required_points: list[str] = Field(min_length=1)
    rubric: list[RubricCriterion] = Field(min_length=1)
    max_score: int = Field(gt=0)
    response_id: str = Field(min_length=1)
    answer_text: str = ""
    final_answer: str | None = None
    answer_image_path: str | None = None
    human_score: int = Field(ge=0)
    human_feedback: str = Field(min_length=1)

    @model_validator(mode="after")
    def validate_scores(self) -> "EvaluationCase":
        if self.human_score > self.max_score:
            raise ValueError("human_score cannot exceed max_score")
        if sum(item.score for item in self.rubric) != self.max_score:
            raise ValueError("rubric criterion scores must sum to max_score")
        return self


class GraderInput(BaseModel):
    """Only the fields an AI grader is allowed to see."""

    model_config = ConfigDict(extra="forbid")

    question_id: str
    subject: str
    topic: str
    question_type: str
    question_text: str
    reference_answer: str
    required_points: list[str]
    rubric: list[RubricCriterion]
    max_score: int
    response_id: str
    answer_text: str
    final_answer: str | None
    answer_image_path: str | None

    @classmethod
    def from_case(cls, case: EvaluationCase) -> "GraderInput":
        # Explicit selection prevents human labels from leaking into the grader.
        return cls(**case.model_dump(include=set(cls.model_fields)))


class GraderOutput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    score: int = Field(ge=0)
    feedback: str = Field(min_length=1)


class RunResult(BaseModel):
    """A grader output persisted separately from the ground-truth data."""

    model_config = ConfigDict(extra="forbid")

    run_id: str
    response_id: str
    grader_version: str
    prompt_version: str
    model: str
    ai_score: int = Field(ge=0)
    ai_feedback: str
    latency: float = Field(ge=0, description="Wall-clock latency in seconds")
    timestamp: datetime
