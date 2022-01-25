numbs = [57.8, 46.51, 97, 14.02, 18.34, 45.11, 25, 8877, 134.88, 13]
numbs.sort()
for numb in numbs:
    rub = int(numb)
    kop = (numb - int(numb)) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')
print('\n')
numbs.reverse()
for numb in numbs:
    rub = int(numb)
    kop = (numb - int(numb)) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')

# я не понял как вывести цены пяти самых дорогих товаров по возрастанию
# и не понял как ставить точку в конце последнего значения выводимого списка
