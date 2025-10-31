#define the main method
def main():
  name = input("What's your name?: ")

  #passing the variable name to the hello method
  hello(name)


#define the function/method hello 
def hello(name = "world"):
  print("Hello,", name)


main()