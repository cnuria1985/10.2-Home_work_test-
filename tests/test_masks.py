import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(true_number_card):
    assert get_mask_card_number(true_number_card) == "1234 56** **** 3456"


def test_get_mask_account(true_number_account):
    assert get_mask_account(true_number_account) == "**7890"


def test_get_mask_card_number_symbols():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("bh62345017865435")

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Введите только числовые значения подряд"


def test_get_mask_account_symbols():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("bh62345017865435")

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Введите только числовые значения подряд"


def test_get_mask_card_number_count():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("987450178654399995")

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Неверное количество символов"


def test_get_mask_account_count():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("987450178654399995")

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Неверное количество символов"
