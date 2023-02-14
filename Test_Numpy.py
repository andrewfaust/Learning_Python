import numpy as np

arr = np.arange(15)
print(arr, 'Исходный массив')
arr = arr.reshape(3, 5)
print(arr)
print('Транспонирование')
print(np.transpose(arr))
print(arr.mean(axis = 0))
print(arr.mean(axis = 1))

print('Обратно')
print(arr.reshape(15,))
print('Среднее:', np.mean(arr))
print('Сумма:', np.sum(arr))


numbers = Series([1, -3, 2, 7])
print(numbers)