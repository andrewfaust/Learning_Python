from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt


all_cars = pd.read_csv('/home/Andrew/Документы/Python_code/auto-mpg-quiz.csv',
                       delimiter=',',
                       index_col='name',
                       nrows=40,
                       decimal='.',
                       usecols=['name', 'hp', 'cyl', 'weight', 'accel'])
print(all_cars)

x = all_cars['weight']
y = all_cars['hp']
colors = all_cars['accel']
area = all_cars['cyl'] ** 2

plt.scatter(x, y, s=area, c=colors, cmap='winter')
plt.show()