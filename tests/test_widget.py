import pytest

from src.widget import get_date, mask_account_card

# pytest tests/test_widget.py
# для даты


@pytest.mark.parametrize(
    "date_init, result_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("0001-01-01T02:26:18.671407", "01.01.0001"),
        ("9999-12-31T02:26:18.671407", "31.12.9999"),
    ],
)
def test_get_date_param(date_init, result_date):
    assert get_date(date_init) == result_date


# для карт и счетов
@pytest.mark.parametrize(
    "number_card, result_number",
    [
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
        ("Счет 12345678901234567895", "Счет **7895"),
    ],
)
def test_mask_account_card(number_card, result_number):
    assert mask_account_card(number_card) == result_number
