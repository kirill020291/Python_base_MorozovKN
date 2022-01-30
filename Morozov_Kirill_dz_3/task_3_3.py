from collections import defaultdict


def thesaurus(*args) -> dict:
    dict_out = {}  # результирующий словарь значений
    for name in args:
        first_letter = name[0]
        if first_letter not in dict_out:
            dict_out[first_letter] = []  # создаем пустой список, чтобы потом туда добавить значение
        dict_out[first_letter].append(name)
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))


def thesaurus_2(*args) -> dict:
    # так можно не создавать пустой список, он создается по факту обращения к несуществующему ключу
    dict_out = defaultdict(list)
    for name in args:
        first_letter = name[0]
        dict_out[first_letter].append(name)
    return dict_out


print(thesaurus_2("Иван", "Мария", "Петр", "Илья"))
