# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#     Пример:
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

num = int(input('Введите целое число: '))
def kod (num):
    res = ''
    if num > 0:
        while num != 0:
            res = str(num % 2) + res
            num //= 2
        print(f'Двоичное число: {res}')
    else: print('Введено неверное число.')
kod(num)
