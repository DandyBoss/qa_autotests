import pytest
from base_5 import is_palindrome

@pytest.mark.parametrize("s,exp",[
    ("A man a plan a canal Panama","No"),
    ("TENET",'Yes'),
    ("Довод","Yes"),
    ("Комок","Yes"),
    ("Я иду с мечем судия","No"),
    ("1235","No"),
    ("1221","Yes"),
])
def test_is_palindrome(s,exp):
    assert is_palindrome(s) == exp