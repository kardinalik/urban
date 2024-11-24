'''[ ] Атрибут объекта model - название автомобиля (строка).
[ ] Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень
доступа private.
[ ] Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет
его на корректность. Возвращает True, если корректный, в других случаях
выбрасывает исключение. Уровень доступа private.
[ ] Атрибут __numbers - номера автомобиля (строка).
[ ] Метод __is_valid_numbers(numbers) - принимает numbers и проверяет
его на корректность. Возвращает True, если корректный, в других случаях
выбрасывает исключение. Уровень доступа private.
[ ] Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты
которых обладают атрибутом message - сообщение, которое будет выводиться
при выбрасывании исключения.'''

class Car:
     def __init__(self, model: str, vin: int, numbers: int):
         self.model = model
         if self.__is_valid_vin(vin):
             self.__vin = vin  # vin номер автомобиля
         if self.__is_valid_numbers(numbers):
             self.__numbers = numbers  # номера автомобиля (строка)


     def __is_valid_vin(self, vin_number):
         '''проверяет на корректность vin номер'''
         if not isinstance(vin_number, int):
             raise IncorrectVinNumber('Некорректный тип vin номер')
         elif len(str(vin_number)) != 7:
             raise IncorrectVinNumber('Неверный диапазон для vin номера')
         else:
             return True

     def __is_valid_numbers(self, numbers):
         '''проверяет на корректность номера автомобиля'''
         if not isinstance(numbers, str):
             raise IncorrectCarNumbers('Некорректный тип данных для номеров')
         elif len(numbers) != 6:
             raise IncorrectCarNumbers('Неверная длина номера')
         else:
             return True

class IncorrectVinNumber(Exception):
     def __init__(self, message):
         self.message = message


class IncorrectCarNumbers(Exception):
     def __init__(self, message):
         self.message = message


def createCar(model: str, vin: int, numbers: str) -> Car:
     '''
     Возвращает объект Car, если данные корректны.
     Иначе - None
     '''
     try:
         car = Car(model, vin, numbers)
     except (IncorrectVinNumber, IncorrectCarNumbers) as exc:
         print(exc.message)
         return None
     else:
         print(f'{car.model} успешно создан')
         return car

try:
   first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
   print(exc.message)
except IncorrectCarNumbers as exc:
   print(exc.message)
else:
   print(f'{first.model} успешно создан')

try:
   second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
   print(exc.message)
except IncorrectCarNumbers as exc:
   print(exc.message)
else:
   print(f'{second.model} успешно создан')

try:
   third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
   print(exc.message)
except IncorrectCarNumbers as exc:
   print(exc.message)
else:
   print(f'{third.model} успешно создан')