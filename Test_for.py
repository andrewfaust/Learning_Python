person = {'name': 'Степан', 'gender': 'муж', 'age': 20}
print(person)
for key, value in person.items():
    print('Ключ: ', key)
    print('Значение: ', value)

favorite_fruit = {'Дима': 'персик',
                  'Алексей': 'манго',
                  'Елена': 'яблоко',
                  'Антон': 'ананас'}
for name, fruit in favorite_fruit.items():
    print(name, 'любит есть', fruit)


