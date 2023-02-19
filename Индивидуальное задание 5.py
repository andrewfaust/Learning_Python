from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

answers = pd.read_csv('/home/Andrew/Документы/Python_code/answers1.csv')


to_plot = pd.DataFrame(answers['Choice_1'].value_counts())
to_plot.columns = ['Amount']
to_plot = to_plot.sort_index()

print(to_plot)

#plt.bar(to_plot.index, to_plot['Amount'])


vertical_stack = pd.concat([to_plot.iloc[2:], to_plot.iloc[:2]], axis=0)
vertical_stack.index = ['Анализ\n текстов', 'Визуализация\n данных', 'Машинное\n обучение',
       'Методы\n искусственного\n интеллекта', 'Ничего из\n перечисленного',
       'Обработка\n изображений', 'Статистика', 'Электронные\n таблицы',
       'Big Data', 'Python']
plt.bar(vertical_stack.index, vertical_stack['Amount'])
plt.xticks(rotation='vertical')
plt.show()