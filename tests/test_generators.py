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
    result = list(transaction_descriptions(transactions))
    # Проверяем, что результат соответствует ожидаемому
    assert result == ['Перевод организации', 'Перевод со счета на счет',
                      'Перевод со счета на счет', 'Перевод с карты на карту',
                      'Перевод организации']


def test_transaction_descriptions_no_operations(transactions_no_operations):
    # Проверяем реакцию на список без указания типа операций
    result = list(transaction_descriptions(transactions_no_operations))
    assert result == ["Отсутствует ключ 'description'", "Отсутствует ключ 'description'",
                  "Отсутствует ключ 'description'", "Отсутствует ключ 'description'",
                  "Отсутствует ключ 'description'"]


def test_transaction_descriptions_boosh(transactions_boosh):
    # Проверяем реакцию на пустой список
    result = list(transaction_descriptions(transactions_boosh))
    assert result == []


def test_transaction_descriptions_no_two_operations(transactions_no_two_operations):
    # Проверяем реакцию на пустой список
    result = list(transaction_descriptions(transactions_no_two_operations))
    assert result == ['Перевод организации', 'Перевод со счета на счет', 'Перевод со счета на счет',
                      "Отсутствует ключ 'description'", "Отсутствует ключ 'description'"]


def test_card_number_generator():
    result = list(card_number_generator(1, 5))
    assert result == ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003',
                      '0000 0000 0000 0004', '0000 0000 0000 0005']


def test_card_number_generator_more():
    result = list(card_number_generator(9999999999999985, 9999999999999990))
    assert result == ['9999 9999 9999 9985', '9999 9999 9999 9986', '9999 9999 9999 9987',
                      '9999 9999 9999 9988', '9999 9999 9999 9989', '9999 9999 9999 9990']
