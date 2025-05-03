import pytest

from src.widget import get_date


@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-25T15:30:00", "25.12.2023"),
        ("2000-01-01T00:00:00", "01.01.2000"),
        ("1999-07-04T12:45:30", "04.07.1999"),
        ("2010-10-10T10:10:10", "10.10.2010"),
    ],
)
def test_get_date(input_date: str, expected_output: str) -> None:
    """Тестирует преобразование даты в формат DD.MM.YYYY."""
    assert get_date(input_date) == expected_output


if __name__ == "__main__":
    pytest.main()
