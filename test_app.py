
from app import add, subtract

def test_add():
    result = add(2, 3)
    assert result == 5

def test_subtract():
    result = subtract(5, 2)
    assert result == 3
