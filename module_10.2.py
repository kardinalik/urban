"""
[x] Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
[x] Атрибут name - имя рыцаря. (str)
[х] Атрибут power - сила рыцаря. (int)
[х] А также метод run, в котором рыцарь будет сражаться с врагами:
[х] При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
[] Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
[] В процессе сражения количество врагов уменьшается на power текущего рыцаря.
[] По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>...,
осталось <кол-во воинов> воинов."
[] После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"""

from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            sleep(1)
            days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f'{self.name} сражается {days} дней, осталось {enemies} воинов врага.')
        print(f'{self.name} одержал победу спустя {days} дней!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все сражения закончены!")