def num_translate(value):
    translations = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
    }
    if value not in translations:
        return None
    str_out = translations[value]
    return str_out


print(num_translate("one"))
print(num_translate("eight"))
