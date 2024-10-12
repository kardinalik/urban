"""
[v] Создайте класс House.
[v] Вунтри класса House определите метод __init__, в который передадите
название и кол-во этажей.
[v] Внутри метода __init__ создайте атрибуты объекта self.name и
self.number_of_floors, присвойте им переданные значения.
[v] Создайте метод go_to с параметром new_floor и напишите логику внутри
него на основе описания задачи.
[v] Создайте объект класса House с произвольным названием и количеством
этажей.
[v] Вызовите метод go_to у этого объекта с произвольным числом.
"""

class House:
     def __init__(self, name, number_of_floors):
         self.name = name
         self.number_of_floors = number_of_floors
         # Проверка работы:
         # print(f'Добро пожаловать в {self.name}! количество этажей:{self.number_of_floors}')


     def go_to(self, new_floor):
         if 0 < new_floor <= self.number_of_floors:
             for floor in range(1, new_floor + 1):
                 print(floor)
         else:
             print('Такого этажа не существует')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
