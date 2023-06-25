from pandas import Series, DataFrame
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
link = pd.read_csv('/home/Andrew/Документы/Python_code/pulsar_stars_new.csv', delimiter=',')
stars = link
stars_train = stars[((stars['TG'] == 0) & (stars['MIP'] >= 94.6640625) & (stars['MIP'] <= 95.2890625)) |
                    ((stars['TG'] == 1) & (stars['MIP'] >= 65.078125) & (stars['MIP'] <= 70.7421875))]


print(stars_train)
print(stars_train.MIP.mean())

stars_train_normed = (stars_train - stars_train.min())/(stars_train.max() - stars_train.min())
print(stars_train_normed.MIP.mean())

X = pd.DataFrame(stars_train_normed.drop(['TG'], axis=1))
y = stars_train_normed.TG
clf = LogisticRegression(random_state=2019, solver='lbfgs').fit(X, y)

new_star = [0.254, 0.19, 0.939, 0.624, 0.935, 0.875, 0.151, 0.312]
clf.predict_proba([new_star])
print('Вероятность отнесения к классу пульсар: ', clf.predict_proba([new_star])[0][1])

clf.predict([new_star])

neigh = KNeighborsClassifier(n_neighbors = 1, p = 2)
neigh.fit(X, y)
KNeighborsClassifier(n_neighbors=1)
print('Предсказанный класс: ', neigh.predict([new_star])[0])
print('Расстояние до ближайшей звезды: ', neigh.kneighbors([new_star])[0][0][0])











