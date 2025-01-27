def mask_account_card (number_card: str) -> str:
    """Функция, возвращающая замаскированный номер карты или счёта"""

    schet = "Счет"
    if schet in number_card:
        return f"Счет **{number_card[-4:]}"
    else:
        list_name_card = number_card.split()
        name_card = []
        for i in list_name_card:
            if i.isalpha():
                name_card+=i
            elif i.isdigit():
                numbers_card = i
        return f"{"".join(name_card)} {numbers_card[0:4]} {numbers_card[4:6]}** **** {numbers_card[-4:]}"

if __name__ == "__main__":
    print(mask_account_card(str("Visa Platinum 2202345612340099")))
    print(mask_account_card(str("Счет 11223344556677889900")))
