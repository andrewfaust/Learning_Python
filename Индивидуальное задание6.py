from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('/home/Andrew/Документы/Python_code/hata.csv',
                       index_col = 'ID')

data = 1 - np.exp(1 - data/data.min())
data['SUM'] = data['DISTANCE'] + data['STOP_COUNT'] + data['COST']
#data_sorted = data.sort_values('SUM', ascending = True).iloc[0:3].index
data_sorted = data.sort_values('SUM', ascending = True)

data1 = data[data['SUM'] < 2]
data1 = data1.reset_index()
print(data1)


fig = plt.subplots(figsize =(20, 7))
p1 = plt.bar(data1.index, data1['DISTANCE'], color = 'darkblue', label = 'DISTANCE')
p2 = plt.bar(data1.index, data1['COST'], bottom = data1['DISTANCE'], color = 'blue', label = 'COST')
p3 = plt.bar(data1.index, data1['STOP_COUNT'], bottom = data1['DISTANCE'] + data1['COST'], color = 'lightblue', label = 'STOP_COUNT')
for i in range(len(data1)):
    plt.annotate(data1['ID'][i], (i, data1['SUM'][i]), size=10, color="black", ha='center', va='bottom')
plt.ylabel('SUM')
plt.title('TITLE')
plt.xticks([])
plt.legend(bbox_to_anchor=(1,1))
plt.show()



#print(data_sorted)
