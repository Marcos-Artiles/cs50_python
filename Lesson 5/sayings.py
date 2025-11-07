def main():
  hello("World")
  goodbye("World")

def hello():
  print(f"Hello, {name}")

def goodbye(name):
  print(f"Goodbye, {name}")

#preventing the call of the method main() until specified
if __name__ == "__main__":
  main()