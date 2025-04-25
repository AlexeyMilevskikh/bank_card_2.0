import pytest
from src.processing.operations import filter_by_state, sort_by_date


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


def test_sort_by_date_descending():
    ops = [
        {'id': 1, 'date': '2022-01-01T00:00:00.000000'},
        {'id': 2, 'date': '2023-01-01T00:00:00.000000'},
        {'id': 3, 'date': '2021-01-01T00:00:00.000000'}
    ]
    result = sort_by_date(ops)
    assert [op['id'] for op in result] == [2, 1, 3]

def test_sort_by_date_ascending():
    ops = [
        {'id': 1, 'date': '2022-01-01T00:00:00.000000'},
        {'id': 2, 'date': '2023-01-01T00:00:00.000000'},
        {'id': 3, 'date': '2021-01-01T00:00:00.000000'}
    ]
    result = sort_by_date(ops, reverse=False)
    assert [op['id'] for op in result] == [3, 1, 2]

def test_sort_by_date_with_missing_key():
    ops = [
        {'id': 1, 'date': '2022-01-01T00:00:00.000000'},
        {'id': 2}  # Нет ключа date
    ]
    with pytest.raises(KeyError):
        sort_by_date(ops)