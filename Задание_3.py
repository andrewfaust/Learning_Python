from pandas import Series, DataFrame
import pandas as pd

all_cars = pd.read_csv('/home/Andrew/Документы/Python_code/auto-mpg-quiz.csv', index_col = 'name')

print(all_cars)



#all_cars['hp_kW'] = round(all_cars['hp'] * 0.7355, 1)
#all_cars.sort_values(by=['hp'], ascending=False)
#all_cars = all_cars.drop(['mpg', 'displ', 'yr', 'origin'], axis = 1)

#all_cars[all_cars.cyl == 4]
#all_cars[(all_cars.cyl == 4) & (all_cars.hp > 80)]
#cars_frame = all_cars[((all_cars.cyl == 4) & (all_cars.hp > 80)) | ((all_cars.cyl == 8) & (all_cars.hp > 90))]

#print(cars_frame)

#all_cars = round(cars_frame.weight.mean(), 3) #Среднее + округляем до 3 чисел после запятой

