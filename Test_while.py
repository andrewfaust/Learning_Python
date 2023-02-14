i = 1
while i <= 20:
    j = 1
    while True:
        print(i * j)
        j += 1
        if j > i:
            print('Прерывание внутреннего цикла')
            break
    i += 1
    print('Конец итерации внешнего цикла')
print('Конец цикла')
