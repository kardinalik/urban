"""
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
и "Составное" в противном случае.
"""

def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        sum_ = sum(args)
        counter = 0
        for i in range(2, sum_ // 2 + 1):
            if sum_ % i == 0:
                counter = counter + 1
        if counter <= 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    total = 0
    for i in args:
        total += i
    return total


result = sum_three(2, 3, 6)
print(result)