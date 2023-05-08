import pytest
#from myscript import add_numbers
from math_ops import add_numbers

def test_add_numbers():
    assert add_numbers(5, 10) == 15
    assert add_numbers(0, 0) == 0
    assert add_numbers(-5, 5) == 0