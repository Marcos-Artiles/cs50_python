import sys

if len(sys.argv) < 2:
  sys.exit("Too few arguments")

elif len(sys.argv) > 2:
  sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1])

#using CLA (comand line arguments to run the program)
for arg in sys.argv[1:]:
  print("Hello, my name is", arg)