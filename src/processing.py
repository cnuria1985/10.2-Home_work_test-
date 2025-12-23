from datetime import datetime


def filter_by_state(list_of_dictionaries: list[dict], state: str = "EXECUTED") -> list[dict]:
    "Функция возвращает список словарей, содержащий только те словари, у которых ключ state"
    total_of_dictionary = []
    for dictionary in list_of_dictionaries:
        if state in dictionary["date"]:
            total_of_dictionary.append(dictionary)
    return total_of_dictionary


def sort_by_date(list_of_dictionaries: list[dict], reverse: bool = True) -> list[dict]:
    "Функция возвращает список словарей, отсортированный по дате"

    total_of_dictionary = sorted(
        list_of_dictionaries, key=lambda x: (datetime.strptime(x["date"], "%d.%m.%Y"), x["name"]), reverse=False
    )
    return total_of_dictionary


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"name": "Сергей", "date": "27.08.1985"},
                {"name": "Нурия", "date": "19.11.1985"},
                {"name": "Ракета", "date": "01.03.2020"},
                {"name": "Игорь", "date": "09.06.2010"},
                {"name": "Маруся", "date": "27.02.2015"},
                {"name": "Евгений", "date": "01.12.2011"},
                {"name": "Рыжик", "date": "01.02.2025"},
            ],
            "1985",
        )
    )
    print(
        sort_by_date(
            [
                {"name": "Сергей", "date": "27.08.1985"},
                {"name": "Нурия", "date": "19.11.1985"},
                {"name": "Ракета", "date": "01.03.2020"},
                {"name": "Игорь", "date": "09.06.2010"},
                {"name": "Маруся", "date": "27.02.2015"},
                {"name": "Евгений", "date": "01.12.2011"},
                {"name": "Рыжик", "date": "01.02.2025"},
            ]
        )
    )
