# make some tests for div sub mul and add
from utils import add,mul,sub,div

def test_add():
    assert add(2,3) == 5
    assert add(5,6) == 11

def test_mul():
    assert mul(2,3) == 6
    assert mul(5,6) == 30

def test_sub():
    assert sub(12,6) == 6
    assert sub(6,2) == 4

def test_div():
    assert div(12,6) == 2
    assert div(10,2) == 5
