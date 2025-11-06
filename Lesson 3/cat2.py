#define the main function
def main():
  number = get_number()
  meow(number)

#function that obtains the number from the user if is greater to 0
def get_number():
  while True:
    n = int(input("What's n?: "))
    if n > 0:
      return n

#function that prints "meow"
def meow(n):
  for _ in range(n):
    print("meow")

main()