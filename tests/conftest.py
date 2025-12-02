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
