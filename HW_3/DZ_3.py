# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#     Пример:
#     [1.1, 1.2, 3.1, 5, 10.01] => 0.19

mylist = [1.1, 1.2, 3.1, 5, 10.01]
max = abs(mylist[0]) % 1
min = abs(mylist[0]) % 1
for i in range(1, len(mylist)):
    if max < abs(mylist[i]) % 1:
        max = abs(mylist[i]) % 1
    if min > abs(mylist[i]) % 1:
        min = abs(mylist[i]) % 1
d = round(max - min, 2)
print(d)