from typing import Any, Dict, List

import pytest

from src.processing.operations import filter_by_state, sort_by_date


@pytest.fixture
def sample_operations() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "PENDING"},
    ]


@pytest.mark.parametrize(
    "expected_length, expected_ids",
    [
        (2, [1, 3]),  # Ожидаем 2 операции с состоянием EXECUTED
    ],
)
def test_filter_by_state_default(
    sample_operations: List[Dict[str, Any]], expected_length: int, expected_ids: List[int]
) -> None:
    result = filter_by_state(sample_operations)
    assert len(result) == expected_length
    assert [op["id"] for op in result] == expected_ids


@pytest.mark.parametrize(
    "state, expected_length, expected_id",
    [
        ("CANCELED", 1, 2),  # Ожидаем одну операцию с состоянием CANCELED
    ],
)
def test_filter_by_state_canceled(
    sample_operations: List[Dict[str, Any]], state: str, expected_length: int, expected_id: int
) -> None:
    result = filter_by_state(sample_operations, state)
    assert len(result) == expected_length
    assert result[0]["id"] == expected_id


def test_filter_by_state_empty_result(sample_operations: List[Dict[str, Any]]) -> None:
    assert filter_by_state(sample_operations, "UNKNOWN") == []


@pytest.mark.parametrize(
    "ops, expected_ids",
    [
        (
            [
                {"id": 1, "date": "2022-01-01T00:00:00.000000"},
                {"id": 2, "date": "2023-01-01T00:00:00.000000"},
                {"id": 3, "date": "2021-01-01T00:00:00.000000"},
            ],
            [2, 1, 3],
        ),
    ],
)
def test_sort_by_date_descending(ops: List[Dict[str, Any]], expected_ids: List[int]) -> None:
    result = sort_by_date(ops)
    assert [op["id"] for op in result] == expected_ids


@pytest.mark.parametrize(
    "ops, expected_ids",
    [
        (
            [
                {"id": 1, "date": "2022-01-01T00:00:00.000000"},
                {"id": 2, "date": "2023-01-01T00:00:00.000000"},
                {"id": 3, "date": "2021-01-01T00:00:00.000000"},
            ],
            [3, 1, 2],
        ),
    ],
)
def test_sort_by_date_ascending(ops: List[Dict[str, Any]], expected_ids: List[int]) -> None:
    result = sort_by_date(ops, reverse=False)
    assert [op["id"] for op in result] == expected_ids


def test_sort_by_date_with_missing_key() -> None:
    ops = [{"id": 1}, {"id": 2}]  # Удаляем ключ date для теста
    with pytest.raises(KeyError):
        sort_by_date(ops)
