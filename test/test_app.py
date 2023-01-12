from app import bubble_sort


import pytest

test_data = [
    ([1,4,3,5,136,621,32,13,2], ([1,4,3,5,136,621,32,13,2]).sort()),
    ([1,4,3,24,2,4,5], ([1,4,3,24,2,4,5]).sort()),
    ([-1, -4, 3, -5, -5, 2, -4, -5, 2, -4], ([-1, -4, 3, -5, -5, 2, -4, -5, 2, -4]).sort()),
    ([1,1,1,1,1,1,1,1,], ([1,1,1,1,1,1,1,1,]).sort())
]
@pytest.mark.parametrize('sample, expected_output', test_data)
def test_bubble_sort(sample, expected_output):
    assert bubble_sort(sample) == expected_output