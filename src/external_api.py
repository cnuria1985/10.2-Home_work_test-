
import requests

API_KEY = 'FzJa4aIyB2AB1nMfZqOH5QmChcUw4aSX'
headers = {'apikey': API_KEY}

response = requests.get('https://api.apilayer.com/exchangerates_data/live?base=USD,EUR&symbols=RUB', headers=headers)

def get_convert(transaction):
    if transaction['operationAmount']['currency']['name'] == 'RUB':
        amount_convert = transaction['operationAmount']['currency']['name']

    elif transaction['operationAmount']['currency']['name'] == ('USD', 'EUR'):
        amount_convert = response.json()
    else:
        raise NameError("Not USD, not EUR")

    return amount_convert

# payload = {
#     "amount": "1200",
#     "from": "EUR",
#     "to": "USD"
# }
# headers = {
#     "apikey": "FzJa4aIyB2AB1nMfZqOH5QmChcUw4aSX"
# }
#
# response = requests.get(url, headers=headers, params=payload)

# result = response.json()

# print(result)


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