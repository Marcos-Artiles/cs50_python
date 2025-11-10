import random

cards = ["Jack", "Queen", "King"]

def main():
  #using seed to add randomnes but controlled for debuggin
  random.seed(0)

  #choices with the argument "k" will choose what ever we give in K "with replacement"
  print(random.choices(cards, k = 2))

  #sample is the same but without replacement
  print(random.sample(cards, k = 2))

  #the weights argument makes it more likely for one object to be chosen
  print(random.choices(cards, weights = [75, 20, 5], k = 2))

main()