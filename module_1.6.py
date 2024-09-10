# Задание 1
my_dict = {'Артем' : 1990 , 'Денис' : 1992, 'Сергей' : 1975, 'Павел' : 1991}
print('dict;', my_dict)
print('existing_value;', my_dict['Артем'])
print('not_existing_value;', my_dict.get('Глеб'))
my_dict.update({'Кирилл': 1989 , 'Николай': 1947})
a = my_dict.pop('Николай')
print('deleted_value:', a)
print('modified_dict;', my_dict)
#Задание 2
my_set={'4', 8, '15', 1.6, '15', 8, '4', 1.6}
print('set;', my_set)
my_set.update([23, '42'])
my_set.remove(8)
print('new_set;', my_set)
