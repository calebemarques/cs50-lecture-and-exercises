import pytest

from convert import convert

def test_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000.0
    assert convert(233) == 34856303873100.0 


def test_zero():
    assert convert(0) == 0.0


def test_negative():
    assert convert(-1) == -149597870700.0
    assert convert (-233) == -34856303873100.0 
    assert convert (-50) == -7479893535000.0
 
def test_error():
    with pytest.raises(TypeError):
         convert("1") 
def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2)
    assert convert(0.34)  == pytest.approx(50863276038.0)
