def convert_time(duration: int) -> str:
    return f" {duration // (24 * 60 * 60)} дн {duration // 3600 % 24} час" \
    f" {duration // 60 % 60} мин {duration % 60} сек"

duration = [53, 153, 4153, 35000000]
for i in duration:
    result = convert_time(i)
    print(result)

# я пока не разобрался как реализовать вывод только секунд или только минут и тд.