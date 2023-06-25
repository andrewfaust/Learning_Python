from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_series = pd.read_csv('/home/Andrew/Документы/Python_code/task7.csv', delimiter=',')
data_series.index += 1 # Индекс начинаем с 1
#data_series['y_exp_norm_user0,15'] = data_series['y'].ewm(alpha=0.15, adjust=False).mean()



#print(data_series)
#print(data_series['y_exp_norm_user0,15'].loc[[44]]) # вывести определенный столбец пятой строки
#print(data_series['y_exp_norm_user0,15'].loc[[100]]) # вывести определенный столбец пятой строки

#plt.figure(figsize=(20, 8))   #Построим график
#plt.plot('y', data = data_series, color = 'g')
#plt.plot('y_exp_norm_user0,15', data = data_series, color = 'r')
#plt.xlabel('Time step')
#plt.ylabel('y')
#plt.legend(bbox_to_anchor=(0,1))
#plt.show()

X = data_series.index.to_numpy()
y = data_series['y'].to_numpy()
poly = np.polyfit(X, y, 1)
a = poly[0]
b = poly[1]
#print(x)
#print(y)
#print(poly)
#print(a,b)

x = np.arange(1, 101)
data_series['lin_trend'] = a * x + b
print(data_series)



plt.figure(figsize=(20, 8))
plt.plot('y', data=data_series)
plt.plot('lin_trend', data=data_series)
plt.xlabel('Time step')
plt.ylabel('y')
plt.show()


f_i = data_series['lin_trend']
y_avg = data_series['y'].mean()
R2 = 1 - ((y - f_i) ** 2).sum() / ((y - y_avg) ** 2).sum()
y_101 = a * 101 + b

print(R2)
print(y_101)
print(a)
print(b)