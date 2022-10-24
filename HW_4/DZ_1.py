# 1. Вычислить число c заданной точностью d
#     Пример:
#     - при d = 0.001, π = 3.141    10^(-1) ≤ d ≤10^(-10)

import math
def f(n):
    p = 0
    for i in range(1,n,4):
        p = (p + 4/i - 4(i+2))
        return p

def pi():
    x = 0.1
    for i in range(1,11):
        print(f"d = {'%.10f' % x}, pi = {round(math.pi,i)}")
        x = x / 10

if __name__ == '__name__':
    n = 10000
    print(n)
