# 1. напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# пример:
# - 6782 -> 23
# - 0,56 -> 11

print('Введите число:')
num = float(input())
length = len(str(num))
i = 0
b = 0
c = 0
while i < length:
    i = i + 1
    num = num / 10
    b = num % 10
    c = c + b
print(int(c))

