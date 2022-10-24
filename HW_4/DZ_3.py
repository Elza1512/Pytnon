# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randrange

def numbers(count: int):
    if count < 0:
        return[]
    list_numbers = []
    for i in range(count):
        list_numbers.append(randrange(count))
    return list_numbers

def elements(list_numbers):
    return set(list_numbers)

all_list = numbers(int(input("Введите размер списка: ")))
print(all_list)
print(elements(all_list))