import unittest
from src.widget import mask_account_card


class TestWidget(unittest.TestCase):

    def test_mask_account(self) -> None:
        # Тесты для информации о счете
        self.assertEqual(mask_account_card("Счет 64686473678894779589"), "Счет **9589")
        self.assertEqual(mask_account_card("Счет 35383033474447895560"), "Счет **5560")
        self.assertEqual(mask_account_card("Счет 73654108430135874305"), "Счет **4305")

    def test_mask_card(self) -> None:
        # Тесты для информации о банковских картах
        self.assertEqual(mask_account_card("Maestro 1596837868705199"), "Maestro 1596 83** **** 5199")
        self.assertEqual(mask_account_card("MasterCard 7158300734726758"), "MasterCard 7158 30** **** 6758")
        self.assertEqual(mask_account_card("Visa Classic 6831982476737658"), "Visa Classic 6831 98** **** 7658")
        self.assertEqual(mask_account_card("Visa Platinum 8990922113665229"), "Visa Platinum 8990 92** **** 5229")
        self.assertEqual(mask_account_card("Visa Gold 5999414228426353"), "Visa Gold 5999 41** **** 6353")


if __name__ == "__main__":
    unittest.main()
