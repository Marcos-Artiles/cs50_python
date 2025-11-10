from hello import hello

def test_argument():
  #using assert to declare the expected output for the given input
  assert hello("David") == "Hello David"
  assert hello() == "Hello World"

def test_default():
  #using assert to declare the expected output for the given input
  assert hello() == "Hello World"