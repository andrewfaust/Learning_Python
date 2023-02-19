from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

all_cars = pd.read_csv('/home/Andrew/Документы/Python_code/auto-mpg-quiz.csv',
                       delimiter=',',
                       index_col='name',
                       decimal='.',
                       usecols=['name', 'hp', 'accel', 'cyl', 'mpg'])

all_cars_sorted = all_cars.sort_values('hp')
print(all_cars_sorted)

#plt.plot('hp', 'accel', data=all_cars_sorted, ls='-', lw='1.5', c='purple', marker='o', label='Линия')
#plt.scatter('hp', 'accel', data=all_cars_sorted)
#plt.bar('hp', 'accel', data=all_cars_sorted)
#plt.xlabel('Мощность (л/с)') #Подпись по оси x
#plt.ylabel('Ускорение') #Подпись по оси Y
#plt.hist('hp', data=all_cars_sorted)

pie_data = all_cars.groupby(['cyl']).count()
plt.pie(pie_data['mpg'], labels=pie_data.index)
plt.show()
