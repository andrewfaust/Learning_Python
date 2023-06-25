import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

token = '1d26f10f-abc3-4b60-add8-8780bb6ff481' # ключ, используемый в данном блокноте, необходимо заменить на свой.

url = 'https://kinopoiskapiunofficial.tech/api/v2.2/films/premieres'
params = {'year': 2023, 'month': 'JUNE'}
r = requests.get(url, headers = {'accept': 'application/json', "X-API-KEY": token}, params = params)

try:
  r = requests.get(url, headers={'accept': 'application/json', "X-API-KEY": token}, params = params) # выполняем запрос
  r.raise_for_status()
except requests.exceptions.HTTPError as err:
  print(err)

result = r.json()  #  получаем представление данных в виде объекта Python

df = pd.json_normalize(result['items'])  # json --> датафрейм
df = df.drop(columns=['posterUrl', 'posterUrlPreview','countries','genres','duration','nameEn'])
df = df.set_index('kinopoiskId')
print(df.sample)
