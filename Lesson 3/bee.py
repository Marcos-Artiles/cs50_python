#declaring a dictionary
WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

#main function
def main():
  print("Welcome to Spelling Bee!: ")
  print("Your letters are: A I P C R H G")

  while len(WORDS) > 0:
    print(f"{len(WORDS)} words left!")
    guess = input("Guess a word: ")

    if guess == "GRAPHIC":
      #words.clear() to clear the dictionary of items
      WORDS.clear()
      print("You've won!")

    if guess in WORDS.keys():
      #WORDS.pop(guess) to erase the user's guess form the dictionary
      points = WORDS.pop(guess)
      print(f"Good job! You sccored {points} points.")
  print("That's the game!")

main()

#WORDS.items() returns the names of the keys and their values