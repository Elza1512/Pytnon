# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

def calculate_1cm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while (not ((greater % x == 0) and (greater % y == 0))):
        greater += 1
    else:
        return greater


if __name__ == '__main__':
    print(calculate_1cm(3, 5))
