import pytest

from src.masks import get_mask_account, get_mask_card_number


# Параметризованные тесты для маскирования номера карты
@pytest.mark.parametrize(
    "card_number, expected",
    [
        (7000792289606361, "7000 79** **** 6361"),
        (1234567812345678, "1234 56** **** 5678"),
        (9876543210123456, "9876 54** **** 3456"),
    ],
)
def test_get_mask_card_number(card_number: int, expected: str) -> None:
    """Тестирует маскирование номера карты."""
    assert get_mask_card_number(card_number) == expected


# Параметризованные тесты для маскирования номера счета
@pytest.mark.parametrize(
    "account_number, expected",
    [
        (73654108430135874305, "**4305"),
        (64686473678894779589, "**9589"),
        (35383033474447895560, "**5560"),
    ],
)
def test_get_mask_account(account_number: int, expected: str) -> None:
    """Тестирует маскирование номера счета."""
    assert get_mask_account(account_number) == expected


if __name__ == "__main__":
    pytest.main()
