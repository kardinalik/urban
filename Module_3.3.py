def print_params(a=1, b="Строка", c=True):
    print(a, b, c)


print('Первое Условие')
print_params(1, 'str', True)
print_params(b=25)
print_params(c=[1, 2, 3])

print()
print("Второе условие")
values_list = ["цифра", 7, 2.5]
values_dict = {'a': 1, 'b': 'str', 'c': True}
print_params(*values_list)
print_params(**values_dict)

print()
print('Третье условие')
values_list_2 = [36.6, 'Температура в норме']
print_params(*values_list_2, True)