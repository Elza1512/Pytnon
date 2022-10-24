# 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def find_s_mult(n):
    s_list = []
    for i in range(2, int(n / 2) + 1):
        for j in range(2, i):
         if i % j == 0:
            break
        else:
            if n % i == 0:
                n = n / i
                s_list.append(i)
    return s_list

def main():
    num = int(input('Введите натуральное число: '))
    s_list = find_s_mult(num)
    if len(s_list) > 0:
        print(f'Число {num} имеет простые множители:')
        print(s_list)
    else:
        print(f'Число {num} является простым...')
main()
