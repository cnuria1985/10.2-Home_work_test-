import requests

# r = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(r.content)
# with open('comic.png', 'wb') as f:
#     f.write(r.content)
#
# import requests

# Задаем адрес сайта, к которому хотим обратиться
# url = "https://e.mail.ru/inbox/"
#
# # Выполняем GET-запрос к сайту и сохраняем ответ в переменную response
# response = requests.get(url)
#
# # Получаем статус-код из ответа и выводим его на экран
# status_code = response.status_code
# print(f"Статус код: {status_code}")
#
# # Проверяем, равен ли статус-код 200, то есть чтобы запрос был успешным
# if status_code == 200:
#     # Выводим содержимое сайта на экран
#     content = response.text
#     print(f"Содержимое сайта:\n{content}")
# else:
#     # Выводим сообщение об ошибке
#     print(f"Запрос не был успешным. Возможная причина: {response.reason}")



# user = "cnuria1985"
# url = f"https://api.github.com/users/{user}/repos"
#
# response = requests.get(url)
#
# repos = response.json()
#
# for repo in repos:
#     if repo["language"] == "Python":
#         print(f"Name: {repo['name']}\nLink: {repo['html_url']}\n")


url = "https://api.apilayer.com/exchangerates_data/convert"

payload = {
    "amount": "1200",
    "from": "EUR",
    "to": "USD"
}
headers = {
    "apikey": "fSHSoKuZ2zVFxstaVw1stEq3GIFqPptc"
}

response = requests.get(url, headers=headers, params=payload)

status_code = response.status_code
result = response.json()

print(status_code)
print(result)
