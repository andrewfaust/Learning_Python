from pandas import Series, DataFrame
import pandas as pd

pulsar_stars = pd.read_csv('/home/Andrew/Документы/Python_code/pulsar_stars_new.csv')

#cars_frame = all_cars[((all_cars.cyl == 4) & (all_cars.hp > 80)) | ((all_cars.cyl == 8) & (all_cars.hp > 90))]

pulsar_frame = pulsar_stars[((pulsar_stars.TG == 0) & (pulsar_stars.MIP >= 81.5234375) & (pulsar_stars.MIP <= 82.9453125))
                           | ((pulsar_stars.TG == 1) & (pulsar_stars.MIP >= 70.7421875) & (pulsar_stars.MIP <= 77.4921875))]
print(pulsar_frame)

pulsar_stars = round(pulsar_frame.MIP.mean(), 3)
print(pulsar_stars)




