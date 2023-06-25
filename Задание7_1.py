from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data_series = pd.read_csv('/home/Andrew/Документы/Python_code/quiz_5_2_3_data.csv', delimiter=',', header=None)
data_series.columns = ["Index", "Row"] # Задаём название столбцов
data_series.index += 1 # Индекс начинаем с 1

def exponential_smoothing(series, alpha):     # сглаженные ряды методом экспоненциального сглаживания (EMA)
    result = [series[0]]
    for index in range(1, len(series)):
        result.append(alpha * series[index] + (1 - alpha) * result[index - 1])
    return result


#data_series['y_exp_norm_user0,1'] = exponential_smoothing(data_series['Row'].to_list(), 0.1)
#data_series['y_exp_norm_user0,3'] = exponential_smoothing(data_series['Row'].to_list(), 0.3)
data_series['y_exp_norm_user0,1'] = data_series['Row'].ewm(alpha=0.1, adjust=False).mean()  # сглаженные ряды методом экспоненциального сглаживания (EMA)
data_series['y_exp_norm_user0,3'] = data_series['Row'].ewm(alpha=0.3, adjust=False).mean()  # сглаженные ряды методом экспоненциального сглаживания (EMA)

plt.figure(figsize=(20, 8))   #Построим график
plt.plot('Row', data = data_series, color = 'g')
plt.plot('y_exp_norm_user0,1', data = data_series, color = 'r')
plt.plot('y_exp_norm_user0,3', data = data_series, color = 'b')
plt.xlabel('Time step')
plt.ylabel('Row')
plt.legend(bbox_to_anchor=(0,1))
plt.show()




#row5 = data_series['y_exp_norm_user0,1'].loc[[5]]
print(data_series)
#print(data_series.loc[[5]]) #Вывести 5 строку или индекс
#print(round(row5, 2))
print(data_series['y_exp_norm_user0,1'].loc[[5]]) # вывести определенный столбец пятой строки
print(data_series['y_exp_norm_user0,3'].loc[[5]])
print(max(abs(data_series['Row'] - data_series['y_exp_norm_user0,1'])))
print(max(abs(data_series['Row'] - data_series['y_exp_norm_user0,3'])))


