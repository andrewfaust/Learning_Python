import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

#page = requests.get('https://itmo.ru/ru/department_units/obschaya_struktura_universiteta.htm')
#print(page.text)

#html_doc = BeautifulSoup(page.text, 'html.parser')
#for tag in html_doc.find('h1', text = 'Основные образовательные и научные подразделения').findNext('div').find_all('ul', recursive = False):
 #print(tag.find('a').text)

xml = requests.get('https://www.cbr-xml-daily.ru/daily_eng.xml')  #API курс валют Сбербанка
#print(xml.status_code)
#print(xml.headers)
#print(xml.headers['Date'])
#print(xml.headers['date'])

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