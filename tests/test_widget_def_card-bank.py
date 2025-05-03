import unittest
from typing import List, Tuple

import pytest

from src.widget import mask_account_card


class TestWidget(unittest.TestCase):

    def setUp(self) -> None:
        """Фикстура, которая будет выполняться перед каждым тестом."""
        self.account_tests: List[Tuple[str, str]] = [
            ("Счет 64686473678894779589", "Счет **9589"),
            ("Счет 35383033474447895560", "Счет **5560"),
            ("Счет 73654108430135874305", "Счет **4305"),
        ]

        self.card_tests: List[Tuple[str, str]] = [
            ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
            ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
            ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
            ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
            ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ]

    def test_mask_account(self) -> None:
        """Тесты для информации о счете."""
        for account_info, expected in self.account_tests:
            with self.subTest(account_info=account_info):
                self.assertEqual(mask_account_card(account_info), expected)

    def test_mask_card(self) -> None:
        """Тесты для информации о банковских картах."""
        for card_info, expected in self.card_tests:
            with self.subTest(card_info=card_info):
                self.assertEqual(mask_account_card(card_info), expected)


if __name__ == "__main__":
    pytest.main()
