import numpy as np
import pandas as pd
from pandas import Series, DataFrame


list = [5, 4, 6, 2, 1, 1, 5, 2, 5, 9, 7]

numbers = pd.Series(list)
Mean = numbers.mean()    #Среднее значение
Median = numbers.median()   #Медиана
Mode = numbers.mode()[0]   # index 1 gives the next mode (ie, 2)  Мода значение
#print(Mean, Median, Mode, sep = '\n') # sep = '\n' вывод по вертикали
#print(max(list)-min(list)) #Размах

print(round(np.log(121), 2))
print(round(np.log(4589), 2))
print(round(np.log(112), 2))
print(round(np.log(345), 2))



#Осталось найти дисперсию 6.61 и стандартное отклонение 2.57






#list_avg = np.average(list) #Среднее значение
#list_mediana = np.median(list) #Медиана
#print(round(list_avg, 2)) #round округлить
#print(list_mediana)



