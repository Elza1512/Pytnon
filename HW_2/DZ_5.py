from random import randint

def func (N):
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    res = []
    for i in range(len(lst)):
        index = randint(0, len(lst) -1)
        res.append(lst[index])
        lst.remove(lst[index])
    print(res)


if __name__== "__main__":
    number = int(input("Число: "))
    func(number)