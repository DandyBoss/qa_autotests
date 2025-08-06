"""
Дан не отсортированный массив целых чисел, который изначально содержит все числа в диапазоне от 1 до N.
К сожалению, из-за неизвестной ошибки, какое-то число стало повторяться, а какое-то число - исчезло.
Примеры:
Было: int[] {1, 2, 3, 4}
Стало: int[] {1, 2, 2, 4}
Было: int[] {1, 2, 3, 4}
Стало: int[] {2, 1, 3, 2}
{1, 2, 2, 3}
На вход вашего метода попадает массив integer-чисел nums, который содержит указанную ошибку.
Ваша задача найти дублирующееся и отсутствующее в изначальном диапазоне числа.
Ограничения:
2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4
Сигнатура: int[] findErrorNums(int[] nums)
"""
from random import randint,choice,random
import copy
def findErrorNums(nums):
    n = len(nums)
    sum1n = (n*(n+1))/2
    sum2 = 0
    t = set()
    double = None
    for i in nums:
        sum2 += i
        if i in t:
            double = i
        t.add(i)
    lost = sum1n - sum2 + double
    return [double,lost]