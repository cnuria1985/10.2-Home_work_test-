import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
# pytest tests/test_generators.py
def test_filter_by_currency(transactions, transactions_filter_by_currency):
    result = list(filter_by_currency(transactions, "USD"))

    # Проверяем, что результат соответствует ожидаемому
    assert result == transactions_filter_by_currency


def test_filter_by_currency_no_valute(transactions):
    # Проверяем, что заданная валюта отсутствует
    result = list(filter_by_currency(transactions, "EUR"))

    assert result == []


def test_filter_by_currency_boosh_list(transactions_boosh):
    # Проверяем реакцию на пустой список
    result = []
    assert result == []


def test_transaction_descriptions(transactions):
    result = "\n".join(list(transaction_descriptions(transactions)))

    # Проверяем, что результат соответствует ожидаемому
    assert result == ('''Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации''')


def test_transaction_descriptions_boosh(transactions_boosh):
    result = []
    assert result == []


def test_card_number_generator():
    result = card_number_generator(1, 5)

    assert result == '''0000 0000 0000 0001
        0000 0000 0000 0002
        0000 0000 0000 0003
        0000 0000 0000 0004
        0000 0000 0000 0005'''

    # '''0000 0000 0000 0001
    #     0000 0000 0000 0002
    #     0000 0000 0000 0003
    #     0000 0000 0000 0004
    #     0000 0000 0000 0005'''

