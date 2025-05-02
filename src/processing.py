from typing import List, Dict, Any


def filter_by_state(list_of_dictionaries: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает список словарей, содержащий только те словари, у которых ключ state"""
    total_of_dictionary = []
    for dictionary in list_of_dictionaries:
        if dictionary["state"] == state:
            total_of_dictionary.append(dictionary)
    return total_of_dictionary



def sort_by_date(list_of_dictionaries: list[dict], reverse: bool = True) -> list[dict]:
    """Функция возвращает список словарей, отсортированный по дате"""

    total_of_dictionary = sorted(list_of_dictionaries, key=lambda x: x["date"], reverse=reverse)
    return total_of_dictionary
