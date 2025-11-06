#defining the main function and its functions to run
def main():
  print_column_vert(3)
  print_row(4)
  print_square(3)
  print_square2(4)

#function to print a column
def print_column_vert(height):
  for _ in range(height):
    print("#")

#function to print a row
def print_row(width):
  print("?" * width)

#function that prints a matrix/square
def print_square(size):
  for i in range(size):
    for j in range(size):
      print("#", end = "")
    print()

#function that prints a matrix/square but the sintax is more simple
def print_square2(size):
  for i in range(size):
    print("#" * size)

main()