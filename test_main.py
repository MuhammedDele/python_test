import pytest
from main import add , subtract , divide 

def test_add():
    assert add(3, 4) ==7

def  test_subtract():
    assert subtract(5, 1)==4

def test_divide():
    # with pytest.raises(ValueError):
    #     divide(6, 0)
    assert divide(8, 2) == 4