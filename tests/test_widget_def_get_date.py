import unittest

from src.widget import get_date


class TestGetDate(unittest.TestCase):
    def test_get_date(self) -> None:
        # Тестовые случаи
        self.assertEqual(get_date("2024-03-11T02:26:18.671407"), "11.03.2024")
        self.assertEqual(get_date("2023-12-25T15:30:00"), "25.12.2023")
        self.assertEqual(get_date("2000-01-01T00:00:00"), "01.01.2000")
        self.assertEqual(get_date("1999-07-04T12:45:30"), "04.07.1999")
        self.assertEqual(get_date("2010-10-10T10:10:10"), "10.10.2010")


if __name__ == "__main__":
    unittest.main()
