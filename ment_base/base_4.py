"""Функция создает матрицу 3x3 и заполняет ее числами от 1 до n.

Создать вариант функции где можно расширять размер матрицы и заполнять ее случайными числами от -15 до n."""
from random import randint
def matrix(m,n):
    if m<0 or n<1:
        return "wrong input"
    else:
        for i in range(1, m+1):
            for j in range(1, n+1):
                x = randint(-15, n)
                print(x, end=' ')
            print("")
matrix(3,3)
