import pytest

from local_delegate_mcp.client import LlamaCppClient, Settings


def test_rejects_empty_input():
    client = LlamaCppClient(Settings(max_input_chars=100))
    with pytest.raises(ValueError, match="must not be empty"):
        client._guard_input("   ", "")


def test_rejects_oversized_input():
    client = LlamaCppClient(Settings(max_input_chars=10))
    with pytest.raises(ValueError, match="limit is 10"):
        client._guard_input("1234567890", "x")
