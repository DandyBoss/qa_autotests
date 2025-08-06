import pytest
from base_7 import twoSum
@pytest.mark.parametrize("nums, target, exp",[
    ([2, 4, 6, 1, 8], 5, ("1", "3")),
    ([3, 2, 4], 6, ("1", "2")),
    ([3, 3], 6, ("0", "1")),
    ([-1, -2, 3], 1, ("1", "2")),
    ([-5, 10, 3], 5, ("0", "1")),
    ([0, 4, 3, 0], 0, ("0", "3")),
    ([10, 0, -10], 0, ("0", "2")),
    ([5, 5, 5, 2], 7, ("0", "3")),
])

def test_twoSum(nums, target, exp):
    result = twoSum(nums, target)
    assert set(result) == set(exp)


@pytest.mark.parametrize("nums, target", [
    ([], 5),
    ([1, 2, 3], 10),
    ([10, 20, 30], 60),
    ([-1, -2, -3], 1),
    ([5], 5),
])
def test_twoSum_no_res(nums, target):
    assert twoSum(nums, target) is None