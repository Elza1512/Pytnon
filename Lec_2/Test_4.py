# 1. Семинар 4(1) Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

list = []
s = ' 12 11 15 2 6 9 8 17 9 0'
list = s.split()
print(list)
max = int(list[0])
min = int(list[0])
for i in range(len(list)):
    if int(list[i]) > max:
        max = int(list[i])
    elif int(list[i]) < min:
        min = int(list[i])
print(f'Наибольшее число {max}, наименьшее число {min}')

exit()
# По простому
print('Введите число')
a = str(input())
b = a.split()
result = []
for i in b:
    result.append(int(i))
print(result)
s = max (result)
d = min(result)
print(s, d)