import sys
from sayings import hello

#importing my own method from my sayings module
if len(sys.argv) == 2:
  hello(sys.argv[1])