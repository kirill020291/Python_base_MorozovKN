"""
1. Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2
"""

my_list = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]


def my_type():
    for i in range(len(my_list)):
        print(type(my_list[i]))


my_type()
