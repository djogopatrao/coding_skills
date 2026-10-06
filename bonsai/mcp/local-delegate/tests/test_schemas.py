import pytest
from pydantic import ValidationError

from local_delegate_mcp.schemas import AnalysisOutput, RequirementsOutput


def test_analysis_confidence_is_bounded():
    with pytest.raises(ValidationError):
        AnalysisOutput(behavior="x", confidence=1.5)


def test_requirement_ids_are_structured():
    with pytest.raises(ValidationError):
        RequirementsOutput(requirements=[{
            "id": "REQ-1",
            "text": "Do thing",
            "kind": "functional",
            "evidence": "user said so",
        }])
