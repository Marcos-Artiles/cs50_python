#code for testing and debugging
def main():
  height = int(input("Height: "))
  pyramid(height)

def pyramid(n):
  for i in range(n):
    #here is the bug
    print("#" * i)

    #the solution is print("#" * (i + 1))

if __name__ == "__main__":
  main()