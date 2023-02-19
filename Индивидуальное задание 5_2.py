from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

answers = pd.read_csv('/home/Andrew/Документы/Python_code/answers1.csv')
colums1 = pd.DataFrame(answers.values.reshape(-1))[0].value_counts()
#print(answers.values.reshape(-1)) # Перевод в одну колонку
#print(colums1)

full_to_plot = pd.DataFrame(pd.DataFrame(answers.values.reshape(-1))[0].value_counts())
full_to_plot.columns = ['Amount']
full_to_plot = full_to_plot.sort_index()
print(full_to_plot)

#plt.pie(full_to_plot['Amount'], labels=full_to_plot.index, autopct='%0.1f%%') # %0.2f%%  Это проценты и два знака после запятой
#plt.show()

plt.rcParams["figure.figsize"] = (16,16) #Размер картинки

plt.subplot(1, 2, 1)

plt.title('FIRST PLOT')
plt.pie(full_to_plot['Amount'], labels=full_to_plot.index, autopct='%0.2f%%')

plt.subplot(1, 2, 2)
plt.title('SECOND PLOT')
plt.pie(full_to_plot['Amount'], labels=full_to_plot.index, autopct='%0.0f%%', rotatelabels=True)

plt.tight_layout()

plt.show()
