def main():
  #passing the function the prompt that the user is giving
  x = get_int("What's X?: ")
  print(f"X is {x}")

#accepting the prompt into the function and doing the logic of asking for an integer
def get_int(prompt):
  while True:
    try:
      x = int(input(prompt))
      
    except ValueError:
      #can use "pass" to do nothing when the error is raised
      print("X is not an integer")

    else:
      return x

main()

#can use "raise" to raise an error myself