"""
Необходимо дополнить класс House следующими специальными методами:
[v] __len__(self) - должен возвращать кол-во этажей здания
self.number_of_floors.
[ ] __str__(self) - должен возвращать строку: "Название: <название>,
кол-во этажей: <этажи>
"""

class House:
     def __init__(self, name, number_of_floors):
         self.name = name
         self.number_of_floors = number_of_floors
         # Проверка работы:
         # print(f'Добро пожаловать в {self.name}! количество этажей:{self.number_of_floors}')


     def go_to(self, new_floor):
         if 0 < new_floor <= self.number_of_floors:
             for floor in range(1 , new_floor + 1):
                 print(floor)
         else:
             print('Такого этажа не существует')


     def __len__(self):
         return self.number_of_floors


     def __str__(self):
         return f'Название: {self.name}. количество этажей:{self.number_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))