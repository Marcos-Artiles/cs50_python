import pytest
from convert import convert

#testing the convert method
def test_conversion():
  assert convert(1) == 149597870700
  assert convert(50) == 7479893535000

#testing the condition for the error raised
def test_error():
  with pytest.raises(TypeError):
    convert("1")

#testing float conversion with tolerance " 1e-'number' "
def test_float_conversion():
  assert convert(0.001) == pytest.approx(149597870.691, abs = 1e-12)