
import json
import os
from dotenv import load_dotenv
import requests

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной GITHUB_TOKEN из .env-файла
#github_token = os.getenv('GITHUB_TOKEN')

# Создание заголовка с токеном доступа API
# headers = {
#     'Authorization': f'token {github_token}'
# }

# Отправка GET-запроса к API
#API = requests.get('https://api.github.com/user', headers=headers)

# Получение API_KEY

API_true = os.getenv('API_KEY')

def get_convert(transaction):
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    if transaction['operationAmount']['currency']['name'] == 'RUB':
        amount_convert = transaction['operationAmount']['amount']
    elif transaction['operationAmount']['currency']['name'] in ['USD', 'EUR']:
        # Get the exchange rate data for the transaction currency to RUB
        base = transaction['operationAmount']['currency']['name']
        symbols = 'RUB'
        amount_convert = get_exchange_rate(base, symbols)
    else:
        raise NameError("Not USD, not EUR")
    return amount_convert


def get_exchange_rate(base, symbols):
    payload = {
         "amount": transaction['operationAmount']['amount'],
         "from": base,
         "to": symbols
    }
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={symbols}&from={base}"
    headers = {"apikey": API_true}
    response = requests.get(url, headers=headers, params=payload)
    result = response.json()
    amount = result['result']
    return amount


if __name__ == "__main__":
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
   }
    print(get_convert(transaction))