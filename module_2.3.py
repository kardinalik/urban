my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0
count = 0
while count < len(my_list):
    if num > my_list[count]:
        break
    elif num == my_list[count] and num != 0:
        print(num)
        count += 1
        num = 0
    elif num < my_list[count]:
        num += 1
    else:
        count += 1

print("all done")


# Решение задачи через цикл FOR
# for num in my_list:
#     if num > 0:
#         print(num)
#     elif num == 0:
#         continue
#     else:
#         break
# print('all done')




