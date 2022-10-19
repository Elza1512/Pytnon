# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     Пример:
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

mylist = [2, 3, 4, 5, 6]
max = abs(mylist[0])
min = abs(mylist[-1])
for i in range(0, 5):
    if max < abs(mylist[i]):
        max = abs(mylist[i])
    if min > abs(mylist[i]):
        min = abs(mylist[i])
d = round(max * min)
print(d)


# myList = [2, 3, 4, 5, 6]
# print(myList[0], myList[-1])
# # print(myList)
# l = len(myList)
# elem = []
# for i in range(l):
#     if (l // 2 + 1):
#         elem.append(myList[i])
# print("Список", myList)
# list_length = len(elem)
# prElements = 0
# arr = 1
# for i in range(list_length):
#     prElements *= i
#     # prElements = prElements * elem[i]
# print("Произведение пар чисел: ", prElements)
