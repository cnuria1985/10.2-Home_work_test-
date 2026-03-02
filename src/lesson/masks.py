def get_mask_card_number(number_card: str) -> str:
    """Функция, маскирующая номер карты"""
    return f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(number_card: str) -> str:
    """Функция, маскирующая номер счёта"""
    return f"**{number_card[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(str(2202345612340099)))
    print(get_mask_account(str(22023456123400991234)))
