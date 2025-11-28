
import pytest
from src.processing import filter_by_state, sort_by_date

# pytest tests/test_processing.py
def test_filter_by_state():
    assert filter_by_state([
        {'name': 'Сергей', 'date': '27.08.1985'},
        {'name': 'Нурия', 'date': '19.11.1985'},
        {'name': 'Игорь', 'date': '09.06.2010'},
        {'name': 'Евгений', 'date': '01.12.2011'},
        {'name': 'Маруся', 'date': '27.02.2015'},
        {'name': 'Ракета', 'date': '01.03.2020'},
        {'name': 'Рыжик', 'date': '01.02.2025'}
    ], '1985') == [{'name': 'Сергей', 'date': '27.08.1985'}, {'name': 'Нурия', 'date': '19.11.1985'}]


def test_filter_by_state_nothing():
    assert filter_by_state([
        {'name': 'Сергей', 'date': '27.08.1986'},
        {'name': 'Нурия', 'date': '19.11.1965'},
        {'name': 'Игорь', 'date': '09.06.2010'},
        {'name': 'Евгений', 'date': '01.12.2011'},
        {'name': 'Маруся', 'date': '27.02.2015'},
        {'name': 'Ракета', 'date': '01.03.2020'},
        {'name': 'Рыжик', 'date': '01.02.2025'}
    ], '1985') == []

def test_sort_by_date(data, data_sort):
    assert sort_by_date(data) == data_sort

def test_sort_by_date_rev(data, data_sort_rev):
    assert sort_by_date(data, reverse=False) == data_sort_rev

def test_sort_by_date_analog(data_sort_analog_a, data_sort_analog_b):
    assert sort_by_date(data_sort_analog_a, reverse=False) == data_sort_analog_b

# pytest tests/test_processing.py
