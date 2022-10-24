# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#     Пример:
#     k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0
from random import randint

def func(k):
    file = open('file.txt', 'w')
    n = int(0)
    for i in range(-k, -1):
        n = randint(0, 101)
    if n != 0:
        file.write(str(n))
        file.write('*x^')
        file.write(str(-i))
        file.write('+')
    n = randint(0, 101)
    if n != 0:
        file.write(str(n))
        file.write('*x+')
    n = randint(0, 101)
    if n != 0:
        file.write(str(n))
        file.write('=0')
        file.close()

num = int(input("Введите коэффициент k: "))
func(num)