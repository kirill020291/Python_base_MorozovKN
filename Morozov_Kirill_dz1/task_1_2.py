def sum_list_1(dataset):
    res = 0
    while dataset != 0:
        res += dataset % 10
        dataset //= 10
    return res


my_list = [i ** 3 for i in range(1, 1001, 2)]

result_1 = sum(filter(lambda num: sum_list_1(num) % 7 == 0, my_list))
print(result_1)

result_2 = sum(filter(lambda num: sum_list_1(num + 17) % 7 == 0, my_list))
print(result_2)
