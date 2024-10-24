"""
Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это
любой транспорт, а Sedan(седан) - наследник класса Vehicle.

I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:
[x] Атрибут owner(str) - владелец транспорта. (владелец может меняться)
[x] Атрибут __model(str) - модель (марка) транспорта. (мы не можем
менять название модели)
[x] Атрибут __engine_power(int) - мощность двигателя. (мы не можем
менять мощность двигателя самостоятельно)
[x] Атрибут __color(str) - название цвета. (мы не можем менять цвет
автомобиля своими руками)
А так же атрибут класса:
[x] Атрибут класса __COLOR_VARIANTS, в который записан список допустимых
цветов для окрашивания. (Цвета написать свои)
Каждый объект Vehicle должен содержать следующий методы:
[х] Метод get_model - возвращает строку: "Модель: <название модели
транспорта>"
[х] Метод get_horsepower - возвращает строку: "Мощность двигателя:
<мощность>"
[х] Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
[х] Метод print_info - распечатывает результаты методов (в том же
порядке): get_model, get_horsepower, get_color; а так же владельца в
конце в формате "Владелец: <имя>"
[x] Метод set_color - принимает аргумент new_color(str), меняет цвет
__color на new_color, если он есть в списке __COLOR_VARIANTS, в
противном случае выводит на экран надпись: "Нельзя сменить цвет на
<новый цвет>".
Взаимосвязь методов и скрытых атрибутов:
Методы get_model, get_horsepower, get_color находятся в одном классе с
соответствующими им атрибутами: __model, __engine_power, __color.
Поэтому атрибуты будут доступны для методов.
Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через
объект(self).
Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~
'black').
II. Класс Sedan наследуется от класса Vehicle, а так же содержит
следующие атрибуты:
Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5
пассажиров)

Пункты задачи:
Создайте классы Vehicle и Sedan.
Напишите соответствующие свойства в обоих классах.
Не забудьте сделать Sedan наследником класса Vehicle.
Создайте объект класса Sedan и проверьте, как работают все его методы,
взяты из класса Vehicle.
"""

class Vehicle:
     __COLOR_VARIANTS = ['yellow', 'black', 'purple', 'green', 'blue',
'red']

     def __init__(self, owner: str, model: str, color: str,
engine_power: int):
         self.owner = owner
         self._model = model
         self._engine_power = engine_power
         self._color = color

     def get_model(self):
         return f' Модель; {self._model}'

     def get_horsepower(self):
         return f'Мощность двигателя; {self._engine_power}'

     def get_color(self):
         return f'Цвет; {self._color}'

     def print_info(self):
         print(self.get_model(), self.get_horsepower(),
self.get_color(), f'Владелец; {self.owner}')

     def set_color(self, new_color):
         if new_color.lower() in self.__COLOR_VARIANTS:
             self._color = new_color
         else:
             print(f'нельзя сменить цвет на {new_color}')



class Sedan(Vehicle):
     __PASSENGERS_LIMIT = 5 # (в седан может поместиться только 5 пассажиров)



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
