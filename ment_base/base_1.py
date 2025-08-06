from random import randint
"""
Напишите программу, которая выводит на экран числа от 1 до n включительно. При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz», а вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5,
то программа должна выводить слово «FizzBuzz»
"""
def fizzbuzz(n):
    res = []
    if n>0:
        for i in range(1,n+1):
            if (i%3==0) and (i%5==0):
                res.append("FizzBuzz")
            elif (i%3==0) and (i%5!=0):
                res.append("Fizz")
            elif (i%3!=0) and (i%5==0):
                res.append("Buzz")
            else:
                res.append(str(i))
    return res

if __name__ == "__main__":
    n = int(input())
    for i in fizzbuzz(n):
        print(i)
