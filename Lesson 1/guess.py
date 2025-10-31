#define function get_guess for obtaining the user's guess
def get_guess():
  guess = int(input("Enter a guess: "))
  return guess

#define main function
def main():

  #asign the result of the get_guess method to the variable guess
  guess = get_guess()
  
  #if the condition is met, it will print correct, else is going to print incorrect
  if guess == 50:
    print("Correct!")
  else:
    print("Incorrect!")

main()