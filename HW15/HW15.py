# Підключіться до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ),
# отримайте курс валют і запишіть його в текстовий файл такому форматі (список):
# "[дата створення запиту]"
# 1. [назва валюти 1] to UAH: [значення курсу до валюти 1]
# 2. [назва валюти 2] to UAH: [значення курсу до валюти 2]
# 3. [назва валюти 3] to UAH: [значення курсу до валюти 3]
# ..
# n. [назва валюти n] to UAH: [значення курсу до валюти n]
# P.S.не забувайте про DRY, KISS, SRP та перевірки
import datetime
import json
from requests import sessions


def session_func(method, url):
    with sessions.Session() as session:
        return session.request(method=method, url=url)


current_date = datetime.date.today()
url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json'
file_name_rate = "rate" + '_' + str(current_date) + '.' + 'txt'
rate_response = session_func('GET', url)


with open(file_name_rate, 'wt', encoding='utf-8') as file:
    file.write((str(current_date)) + '\n')
    for elem in json.loads(rate_response.text):
        file.write(f'{elem["txt"]}  to UAH: {elem["rate"]}' + '\n')

