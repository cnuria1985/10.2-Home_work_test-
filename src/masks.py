def get_mask_card_number(number_card: str) -> str:
    """Функция, маскирующая номер карты"""
    if not number_card.isdigit():
        raise ValueError("Введите только числовые значения подряд")
    else:
        if len(number_card) != 16:
            raise ValueError("Неверное количество символов")
    return f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(number_account: str) -> str:
    """Функция, маскирующая номер счёта"""
    if not number_account.isdigit():
        raise ValueError("Введите только числовые значения подряд")
    else:
        if len(number_account) != 20:
            raise ValueError("Неверное количество символов")
    return f"**{number_account[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(str('2202345017865438')))
    print(get_mask_account(str('123234501786543')))