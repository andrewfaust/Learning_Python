from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import plotly.graph_objects as go

data = pd.read_csv('/home/Andrew/Документы/Python_code/SPFB.csv')
data['DATE'] = data['<DATE>'] + ' ' + data['<TIME>']
data['DATE'] = pd.to_datetime(data['DATE'], format="%d/%m/%y %H:%M") #Формат данных преобразовали из строки в ДАТУ

df_filtered = data[data['DATE'].dt.strftime('%Y-%m-%d') == '2018-09-28']
df_filtered = df_filtered.set_index('DATE')
df_filtered = df_filtered[['<OPEN>','<HIGH>','<LOW>','<CLOSE>']]
df_filtered.columns =['open', 'high', 'low', 'close']

d2 = df_filtered.resample('1H').agg({'open':'first',
                                     'high':'max',
                                     'low':'min',
                                     'close':'last'})

print(d2)

fig = plt.subplots(figsize =(20, 7))
up = d2[d2['close'] >= d2['open']]
down = d2[d2['close'] < d2['open']]
col1 = 'lightblue'
col2 = 'pink'
width = .03
width2 = .002
plt.bar(up.index, up.close-up.open, width, bottom=up.open, color=col1)
plt.bar(up.index, up.high-up.close, width2, bottom=up.close, color=col1)
plt.bar(up.index, up.low-up.open, width2, bottom=up.open, color=col1)
plt.bar(down.index, down.close-down.open, width, bottom=down.open, color=col2)
plt.bar(down.index, down.high-down.open, width2, bottom=down.open, color=col2)
plt.bar(down.index, down.low-down.close, width2, bottom=down.close, color=col2)
plt.show()




#print(df_filtered)
#print(data)
#print(type(data['DATE'][1]))




