import pytest
from base_1 import fizzbuzz
from random import randint

@pytest.mark.parametrize("input,exp", [
    (-10,[]),
    (0,[]),
    (1,["1"]),
    (2,["1","2"]),
    (3,["1","2","Fizz"]),
    (5,["1","2","Fizz","4","Buzz"]),
    (15,["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])
])

def test_fizzbuzz(input,exp):
    assert fizzbuzz(input) == exp

def test_fizzbuzz_rand():
    for i in range(6):
        n = randint(1,100)
        res = fizzbuzz(n)
        assert len(res) == n
        for i in range(1,n+1):
            if (i%3==0) and (i%5==0):
                assert res[i-1] == "FizzBuzz"
            elif (i%3==0) and (i%5!=0):
                assert res[i-1] == "Fizz"
            elif (i%3!=0) and (i%5==0):
                assert res[i-1] == "Buzz"
            else:
                assert res[i-1] == str(i)