import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.cbr-xml-daily.ru/daily.xml'       #API курс валют Сбербанка
xml = requests.get(URL)
xml.encoding = 'Windows-1251'
xml_data = BeautifulSoup(xml.text, 'lxml')
data = []
# перебираем
for valute in xml_data.find_all('valute'):
# извлекаем данные
 numcode = valute.findNext('numcode').contents[0]
 charcode = valute.findNext('charcode').contents[0]
 name = valute.findNext('name').contents[0]
 value = valute.findNext('value').contents[0]
 nominal = valute.findNext('nominal').contents[0]
 data.append({'numcode': numcode, 'name': name, 'charcode': charcode,'value': value})

# переводим в датафрейм
print(pd.DataFrame(data))