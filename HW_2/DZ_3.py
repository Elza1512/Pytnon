# 3. Задайте список из n чисел последовательности (1+ 1/n)^n и
# выведите на экран их сумму (округляйте до 3 знаков после запятой).
#     Пример:
#     - Для n = 6: [2, 2.25, 2.37, 2.441, 2.488, 2.522]
#Вывод: 14.031 (2 + 2.25 + 2.37 + 2.441 + 2.448 + 2.522)
print('Введите число N:')
n = int(input())
for n in range(1, (n + 1) - 0):
    f = round((1 + 1/n) ** n, 3)
    print(f)
