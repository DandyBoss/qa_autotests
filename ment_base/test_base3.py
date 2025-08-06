import pytest
from base_3 import factrl

@pytest.mark.parametrize("n,exp",[
    (-1,"input error"),
    (0,1),
    (1,1),
    (2,2),
    (3,6),
    (4,24),
    (5,120),
    (6,720),
    (10,3628800),
])
def test_factrl(n,exp):
    assert factrl(n)==exp
