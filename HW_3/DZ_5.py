# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#     Пример:
#  для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи](https://ru.wikipedia.org/wiki/Негафибоначчи) Число фибоначи в обратную сторону

num = int(input('Введите целое число: '))
def fibonacci (num):
    fibo = []
    a, b = 1, 1
    for i in range(num):
        fibo.append(a)
        a, b, = b, a + b
    a, b = 0, 1
    for i in range(0, num + 1):
        fibo.insert(0, a)
        a, b = b, a - b
    return fibo
fibo = fibonacci(num)
print(fibonacci(num))
print(fibo.index(0))



