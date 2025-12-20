import pytest

# @pytest.fixture
# def number_list():
#     return '12345'
#
# @pytest.fixture
# def number_lst():
#     return [1, 2, 3, 4, 5]

# Фикстура для тестиров.номера карты


@pytest.fixture
def true_number_card():
    return "1234567890123456"


@pytest.fixture
def true_number_account():
    return "12345678901234567890"


@pytest.fixture
def name_and_number_card():
    return "Visa Gold 5999414228426353"


@pytest.fixture
def name_and_number_account():
    return "Счет 73654108430135874305"


@pytest.fixture
def data():
    return [
        {"name": "Сергей", "date": "27.08.1985"},
        {"name": "Нурия", "date": "19.11.1985"},
        {"name": "Ракета", "date": "01.03.2020"},
        {"name": "Игорь", "date": "09.06.2010"},
        {"name": "Маруся", "date": "27.02.2015"},
        {"name": "Евгений", "date": "01.12.2011"},
        {"name": "Рыжик", "date": "01.02.2025"},
    ]


@pytest.fixture
def data_sort():
    return [
        {"name": "Сергей", "date": "27.08.1985"},
        {"name": "Нурия", "date": "19.11.1985"},
        {"name": "Игорь", "date": "09.06.2010"},
        {"name": "Евгений", "date": "01.12.2011"},
        {"name": "Маруся", "date": "27.02.2015"},
        {"name": "Ракета", "date": "01.03.2020"},
        {"name": "Рыжик", "date": "01.02.2025"},
    ]


@pytest.fixture
def data_sort_rev():
    return [
        {"name": "Нурия", "date": "27.08.1985"},
        {"name": "Сергей", "date": "27.08.1985"},
        {"name": "Игорь", "date": "09.06.2010"},
        {"name": "Евгений", "date": "01.12.2011"},
        {"name": "Маруся", "date": "27.02.2015"},
        {"name": "Ракета", "date": "01.03.2020"},
        {"name": "Рыжик", "date": "01.02.2025"},
    ]


@pytest.fixture
def data_sort_analog_a():
    return [
        {"name": "Сергей", "date": "27.08.1985"},
        {"name": "Рыжик", "date": "01.02.2025"},
        {"name": "Нурия", "date": "27.08.1985"},
        {"name": "Евгений", "date": "01.12.2011"},
        {"name": "Маруся", "date": "27.02.2015"},
        {"name": "Ракета", "date": "01.03.2020"},
        {"name": "Игорь", "date": "09.06.2010"},
    ]


@pytest.fixture
def data_sort_analog_b():
    return [
        {"name": "Нурия", "date": "27.08.1985"},
        {"name": "Сергей", "date": "27.08.1985"},
        {"name": "Игорь", "date": "09.06.2010"},
        {"name": "Евгений", "date": "01.12.2011"},
        {"name": "Маруся", "date": "27.02.2015"},
        {"name": "Ракета", "date": "01.03.2020"},
        {"name": "Рыжик", "date": "01.02.2025"},
    ]


@pytest.fixture
def transactions_filter_by_currency():
    return [
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
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


@pytest.fixture
def transactions():
    return [
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


@pytest.fixture
def transactions_boosh():
    return []


@pytest.fixture
def operations():
    return """Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации"""
