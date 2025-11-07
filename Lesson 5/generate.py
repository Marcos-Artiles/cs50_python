#importing 2 new libraries
import random
import statistics

#obtain a random int within the specified range
number = random.randint(1, 10)
print(number)

#flipping a coin
coin = random.choice(["heads", "tails"])
print(coin)

#shuffling a list
cards = ["Jack", "Queen", "King"]
random.shuffle(cards)
for card in cards:
  print(card)

#printing the average value from the data provided
print(statistics.mean([100, 90]))