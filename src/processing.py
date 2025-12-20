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
    # print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    #                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    #                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    #                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]))
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
