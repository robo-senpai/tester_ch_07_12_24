from math_utils import add

def test_add_positive_numbers():
    result = add(1, 2)
    assert result == 3, f"Expected 3, but got {result}"