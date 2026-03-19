import pytest
from labs.lab_1.lab_1c import max_subarray_sum
from labs.lab_1.lab_1d import two_sum

# --- Tests for lab_1c (Maximum Subarray) ---
def test_max_subarray_standard():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_max_subarray_all_negative():
    # Should return the single largest negative number
    assert max_subarray_sum([-5, -2, -9, -1]) == -1

def test_max_subarray_single_element():
    assert max_subarray_sum([5]) == 5

def test_max_subarray_empty():
    assert max_subarray_sum([]) == 0


# --- Tests for lab_1d (Two Sum) ---
def test_two_sum_standard():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_unsorted():
    assert two_sum([3, 2, 4], 6) == [1, 2]

def test_two_sum_same_numbers():
    assert two_sum([3, 3], 6) == [0, 1]

def test_two_sum_no_solution():
    assert two_sum([1, 2, 3], 10) == []
