import pytest
from calculator import square

def main():
  test_possitive()
  test_negative()
  test_zero()

def test_possitive():
    #using assert to declare the expected output for the given input
    assert square(0) == 0
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    #using assert to declare the expected output for the given input
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    #using assert to declare the expected output for the given input
    assert square(0) == 0

def test_str():
    #using assert to declare the expected output for the given input
    with pytest.raises(TypeError):
        square("cat")

#using "pytest test_calculator.py" for testing the code