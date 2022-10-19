# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#     Пример:
#      [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# Range функция

myList = [2, 3, 5, 9, 3]
l = len(myList)
nechet = []
for i in range(l):
    if i % 2 == 1:
        nechet.append(myList[i])
print("Список чисел: ", myList)
list_length = len(nechet)
sumElements = 0
for i in range(list_length):
    sumElements = sumElements + nechet[i]
print("Сумма элементов списка, стоящих в нечетной позиции:", sumElements)


