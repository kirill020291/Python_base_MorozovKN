"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

duration = int(input('Введите количество секунд: '))

sec_value = duration % 86400

day_value = duration // 86400
sec_value %= 86400

hour_value = sec_value // 3600
sec_value %= 3600

min_value = sec_value // 60
sec_value %= 60

if duration >= 86400:
    print('Длительность: ', day_value, 'дн', hour_value, 'час', min_value, 'мин', sec_value, 'сек')
elif 3600 <= duration < 86400:
    print('Длительность: ', hour_value, 'час', min_value, 'мин', sec_value, 'сек')
elif 60 <= duration < 3600:
    print('Длительность: ', min_value, 'мин', sec_value, 'сек')
elif duration < 0:
    print('Вы ввели неверное число')
else:
    print('Длительность: ', sec_value, 'сек')
