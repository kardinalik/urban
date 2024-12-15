"""
[x] Необходимо создать класс Bank со следующими свойствами:
[x] Атрибуты объекта:
[x] balance - баланс банка (int)
[x] lock - объект класса Lock для блокировки потоков.

Методы объекта:
[x] Метод deposit:
[x] Будет совершать 100 транзакций пополнения средств.
[x] Пополнение - это увеличение баланса на случайное целое число от 50
до 500.
[x] Если баланс больше или равен 500 и замок lock заблокирован -
lock.locked(), то разблокировать его методом release.
[x] После увеличения баланса должна выводится строка "Пополнение:
<случайное число>. Баланс: <текущий баланс>".
[x] Также после всех операций поставьте ожидание в 0.001 секунды, тем
самым имитируя скорость выполнения пополнения.

Метод take:
[x] Будет совершать 100 транзакций снятия.
[x] Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
[x] В начале должно выводится сообщение "Запрос на <случайное число>".
[x] Далее производится проверка: если случайное число меньше или равно
текущему балансу, то произвести снятие, уменьшив balance на
соответствующее число и вывести на экран "Снятие: <случайное число>.
Баланс: <текущий баланс>".
[x] Если случайное число оказалось больше баланса, то вывести строку
"Запрос отклонён, недостаточно средств" и заблокировать поток методом
acquire.
"""

import threading
import random
import time
from threading import Thread, Lock


class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            y = random.randint(50, 500)
            self.balance += y
            print(f'Пополнение: {y}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            x = random.randint(50, 500)
            print(f'Запрос на {x}')
            if self.balance >= x:
                self.balance -= x
                print(f'Снятие: {x}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен. недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')