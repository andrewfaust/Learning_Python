import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100) #Массив из 100 значений на отрезке [-5, 5]
y_1 = 0.5 * x + 1 #Вычисление функции 0.5x+1 для каждого элемента x
y_2 = np.sin(x) #Вычисление функции sin() для каждого элемента x

plt.plot(x, y_1, c='red', label='$y_1=0.5x+1$')
plt.plot(x, y_2, c='blue', label='$y_2=\sin(x)$')
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.legend(loc='upper left')
plt.grid(c='#BFEFEF', ls='-', lw=0.5)
plt.show()