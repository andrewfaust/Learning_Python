from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

all_cars = pd.read_csv('/home/Andrew/Документы/Python_code/auto-mpg-quiz.csv',
                       delimiter=',',
                       index_col='name',
                       nrows=20,
                       decimal='.',
                       usecols=['name', 'hp', 'cyl', 'weight'])

all_cars = all_cars.sort_values('weight')
print(all_cars)

plt.plot('weight', 'hp', data=all_cars, ls='-', lw='1.5', c='purple', marker='o', label='Линия')
plt.title('Зависимость мощности автомобилей от массы')
plt.xlim(1500, 4500)
plt.ylim(40, 250)
#plt.xticks(np.arange(1500, 5000, step=500))
#plt.xticks([1800, 3000, 4500], ['Легковесный','Среднивесный','Тяжоловесный'])
plt.xlabel('Масса (кг)') #Подпись по оси X
plt.ylabel('Мощность (л/с)') #Подпись по оси Y
plt.legend(loc='lower right') #Отображение легенды в нижнем правом углу
plt.grid(c='#BFEFEF', ls='-', lw=0.5) #Отображение сетки с заданными параметрами типа линий и их цвета
plt.show()
# #8000FF  фиолетовый



#plt.plot([2, 1, 3, 0], [4, 3, 3, 4])
#plt.show()





