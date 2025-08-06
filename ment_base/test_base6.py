import pytest
from base_6 import fibonacci

@pytest.mark.parametrize("n,exp",[
    (-5, ValueError),
    (-4, ValueError),
    (-3, ValueError),
    (-2, ValueError),
    (-1, ValueError),
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (20, 6765),
    (30, 832040),
])
def test_fibonacci(n,exp):
    assert fibonacci(n)==exp
