def get_password(number):
    password = ''
    for i in range(1, int((number + 1) /2)):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password


for n in range (3, 21):
    n = int(input("Введите целое число от 3 до 20: "))
    if n > 20:
        print("неверное число, попробуйте еще раз ")
        continue
    else:
        result = get_password(n)
        print("Пароль: ", result)
        break


