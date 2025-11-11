name = input("What's your name?: ")

#opening/creating a .txt file with the ability to "append" by "a"
with open("names.csv", "a") as file:
  file.write(f"{name}\n")

#opening a .txt file with the ability to "read" by "r"
with open("names.csv", "r") as file:
  lines = file.readlines()

#stripping the extra lines
for line in lines:
  print(f"Hello ", line.rstrip())

#new changes
names = []

with open("names.txt") as file:
  for line in file:
    names.append(line.rstrip())

#can use "reverse = True" to invert the sorting
for name in sorted(names):
  print(f"Hello {name}")