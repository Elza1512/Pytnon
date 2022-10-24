# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     Пример:
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

mylist = [2, 3, 4, 5, 6]
for i in range(len(mylist)):
    if len(mylist) > 1:
        max = (mylist[0])
        min = (mylist[-1])
        mylist.pop(0)
        mylist.pop(-1)
        d = round(max * min)
    else:
        max = mylist[0]
        mylist.pop(0)
        d = round(max * max)
    print(d)

