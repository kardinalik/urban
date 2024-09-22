# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку
# в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится
# в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
# Пункты задачи:
"""" 
[v] Создать переменную calls = 0 вне функций.
[v] Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
[v] Создать функцию string_info с параметром string и реализовать логику работы по описанию.
[v] Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
[v] Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
[v] Вывести значение переменной calls на экран(в консоль)."""

calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [s.lower() for s in list_to_search]


print(string_info('capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
