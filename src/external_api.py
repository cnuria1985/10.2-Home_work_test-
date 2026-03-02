import json
import requests


def get_convert(transaction):
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
    headers = {"apikey": "FzJa4aIyB2AB1nMfZqOH5QmChcUw4aSX"}
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
                "name": "RUB",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
   }
    print(get_convert(transaction))