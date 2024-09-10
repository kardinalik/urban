grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5,
5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(sorted(students))
print(students)
GPA = [sum(sub_list) / len(sub_list) for sub_list in grades]
print(GPA)
GPA_for_students = dict(zip(students, GPA))
print(GPA_for_students)