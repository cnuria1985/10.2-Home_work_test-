def mask_account_card(number_card: str) -> str:
    "Функция, возвращающая замаскированный номер карты или счёта"

    schet = "Счет"
    if schet in number_card:
        return f"Счет **{number_card[-4:]}"
    else:
        list_name_card = number_card.split()
        name_card = []
        for i in list_name_card:
            if i.isalpha():
                name_card += i
            elif i.isdigit():
                numbers_card = i
        return f"{" ".join(list_name_card[:-1])} {numbers_card[0:4]} {numbers_card[4:6]}** **** {numbers_card[-4:]}"


def get_date(date_init: str) -> str:
    "Функция, форматирующая дату"
    use_date = f"{date_init[8:10]}.{date_init[5:7]}.{date_init[0:4]}"
    return use_date


if __name__ == "__main__":
    print(mask_account_card(str("Visa Gold 5999414228426353")))
    print(mask_account_card(str("Счет 73654108430135874305")))
    print(get_date(str("2024-03-11T02:26:18.671407")))
