numbs = range(1, 101)

for i in numbs:
    if i % 10 == 1:
        print(i, "процент")
    elif 1 < i % 10 < 5:
        print(i, "процента")
    else:
        print(i, "процентов")
