#same functionalities that recommendations.py but better writen
def main():
    difficulty = input("Difficult or Casual?: ")
    if difficulty != "Difficult" and difficulty != "Casual":
        print("Enter a valid difficulty.")
        return

    players = input("Multiplayer or Single-player?: ")
    if players != "Multiplayer" and players != "Single-player":
        print("Enter a valid number of players.")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")

def recommend(game):
    print("You might like", game)

main()