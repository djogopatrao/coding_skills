from typing import Literal

from pydantic import BaseModel, Field


class Finding(BaseModel):
    severity: Literal["info", "low", "medium", "high"] = "info"
    statement: str = Field(min_length=1)
    evidence: str = Field(min_length=1)


class SummaryOutput(BaseModel):
    summary: str = Field(min_length=1)
    key_points: list[str] = Field(default_factory=list)
    uncertain_claims: list[str] = Field(default_factory=list)


class AnalysisOutput(BaseModel):
    behavior: str = Field(min_length=1)
    findings: list[Finding] = Field(default_factory=list)
    risks: list[str] = Field(default_factory=list)
    suggested_checks: list[str] = Field(default_factory=list)
    confidence: float = Field(ge=0, le=1)


class TestDraftOutput(BaseModel):
    framework: str = Field(min_length=1)
    test_code: str = Field(min_length=1)
    cases: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)


class TestReviewOutput(BaseModel):
    verdict: Literal["pass", "revise"]
    issues: list[Finding] = Field(default_factory=list)
    missing_coverage: list[str] = Field(default_factory=list)
    suggested_changes: list[str] = Field(default_factory=list)


class ClassificationOutput(BaseModel):
    category: str = Field(min_length=1)
    rationale: str = Field(min_length=1)
    signals: list[str] = Field(default_factory=list)
    confidence: float = Field(ge=0, le=1)


class Requirement(BaseModel):
    id: str = Field(pattern=r"^R[0-9]+$")
    text: str = Field(min_length=1)
    kind: Literal["functional", "nonfunctional", "constraint", "acceptance"]
    evidence: str = Field(min_length=1)


class RequirementsOutput(BaseModel):
    requirements: list[Requirement] = Field(default_factory=list)
    ambiguities: list[str] = Field(default_factory=list)
    out_of_scope: list[str] = Field(default_factory=list)


class DocumentationOutput(BaseModel):
    markdown: str = Field(min_length=1)
    assumptions: list[str] = Field(default_factory=list)
    facts_to_verify: list[str] = Field(default_factory=list)
