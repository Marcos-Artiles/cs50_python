#define a global variable
emoticon = ":("

def main():
  #modify global variable locally
  global emoticon

  say("Is anyone there?: ")
  emoticon = ":)"
  say("Oh, hi!")

def say(phrase):
  print(phrase + " " + emoticon)

main()