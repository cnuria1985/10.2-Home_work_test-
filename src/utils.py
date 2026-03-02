import json
from pathlib import Path
path = Path.cwd().parent / 'data' / 'operations.json'


def get_weather(filepath):
    try:
        with open(filepath, encoding='utf-8') as f:
            try:
                data_pyth = json.load(f)
                print(data_pyth)
            except json.JSONDecodeError:
                print('Ошибка декодирования файла')
    except FileNotFoundError:
        print('Файл не найден')
        return False


if __name__ == '__main__':
    get_weather(path)
