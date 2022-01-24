my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 1


while i < len(my_list):
    my_list.insert(i, '"')
    i += 2
my_list.pop(9)
del my_list[10]
my_list.pop(11)
for i in my_list:
    print(i, end=' ')
