import pytest
from src.processing.operations import filter_by_state


@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "PENDING"},
    ]


def test_filter_by_state_default(sample_operations):
    result = filter_by_state(sample_operations)
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)


def test_filter_by_state_canceled(sample_operations):
    result = filter_by_state(sample_operations, "CANCELED")
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_by_state_empty_result(sample_operations):
    assert filter_by_state(sample_operations, "UNKNOWN") == []
