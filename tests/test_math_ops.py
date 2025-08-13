import pytest
from src.math_ops import add, divide

def test_add_positive():
    assert add(2, 3) == 5
    assert add(1.5, 2.5) == 4.0

def test_add_negative():
    assert add(-1, -2) == -3

def test_divide_positive():
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        divide(10, 0)
