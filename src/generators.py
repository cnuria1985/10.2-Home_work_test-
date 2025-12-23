from typing import Generator


def filter_by_currency(trans: list, valute: str) -> Generator:
    """поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)"""
    return (d for d in trans if d["operationAmount"]["currency"]["code"] == valute)


transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")
for item in usd_transactions:
    print(item)


def transaction_descriptions(trans: list):
    """принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for d in trans:
        operation = d["description"]
        yield operation


descriptions = transaction_descriptions(transactions)
for item in transactions:
    print(next(descriptions))

""">>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации"""


def card_number_generator(number_first: int, number_last: int):
    """принимать начальное и конечное значения для генерации диапазона номеров"""

    number_last_1 = number_last + 1
    for number in range(number_first, number_last_1):
        count_zero = 16 - len(str(number))
        number_card = "0" * count_zero + str(number)
        total_number_card = f"{number_card[:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:]}"
        yield total_number_card

generator = card_number_generator(9999999999999980, 9999999999999990)
for i in generator:
    print(i)


if __name__ == "__main__":
    print(filter_by_currency(transactions, "USD"))
    print(transaction_descriptions(transactions))
    print(card_number_generator(1, 5))
