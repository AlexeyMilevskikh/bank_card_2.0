import unittest
from typing import List, Tuple

from src.masks import get_mask_account, get_mask_card_number


class TestMasks(unittest.TestCase):

    def setUp(self) -> None:
        """Фикстура, которая будет выполняться перед каждым тестом."""
        self.card_number_tests: List[Tuple[int, str]] = [
            (7000792289606361, "7000 79** **** 6361"),
            (1234567812345678, "1234 56** **** 5678"),  # Пример дополнительного теста
            (9876543210123456, "9876 54** **** 3456"),  # Пример дополнительного теста
        ]

        self.account_tests: List[Tuple[int, str]] = [
            (73654108430135874305, "**4305"),
            (64686473678894779589, "**9589"),  # Пример дополнительного теста
            (35383033474447895560, "**5560"),  # Пример дополнительного теста
        ]

    def test_get_mask_card_number(self) -> None:
        """Тесты для маскирования номера карты."""
        for card_number, expected in self.card_number_tests:
            with self.subTest(card_number=card_number):
                self.assertEqual(get_mask_card_number(card_number), expected)

    def test_get_mask_account(self) -> None:
        """Тесты для маскирования номера счета."""
        for account_number, expected in self.account_tests:
            with self.subTest(account_number=account_number):
                self.assertEqual(get_mask_account(account_number), expected)


if __name__ == "__main__":
    unittest.main()
