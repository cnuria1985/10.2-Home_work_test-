import json
from pathlib import Path
import os


def get_weather(filepath):
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях"""
    #path = f'C:/Users/0/PycharmProjects/10.2-Home_work_test-/data/{filepath}'
    try:
        with open(filepath, encoding='utf-8') as f:
            data_pyth = json.load(f)
            print(data_pyth)
        return data_pyth
    except FileNotFoundError:
        print('Файл не найден')
        return False

if __name__ == '__main__':
    get_weather('C:/Users/0/PycharmProjects/10.2-Home_work_test-/data/for_test_1.json')