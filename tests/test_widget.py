import pytest
from src.widget import get_date
#  pytest tests/test_widget_copy_for_date.py
#с параметризацией
@pytest.mark.parametrize("date_init, result_date", [
    ('2024-03-11T02:26:18.671407', '11.03.2024 02:26'),
    ('0001-01-01T02:26:18.671407', '01.01.0001 02:26'),
    ('9999-12-31T02:26:18.671407', '31.12.9999 02:26'),
    ('9999-12-T02:26:18.671407', 'Некорректная дата или формат'),
    ('9999-12-31T02:', 'Некорректная дата или формат')
])
def test_get_date_param(date_init, result_date):
    assert get_date(date_init) == result_date