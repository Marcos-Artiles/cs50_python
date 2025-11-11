import csv

with open("students.csv") as file:
  for line in file:
    name, house = line.rstrip().split(",")
    print(f"{name[0]} is in {house[1]}")

#new logic
students = []

with open("students.csv") as file:
  for line in file:

    #dual assing to "name" and "house" while stripping and spliting
    name, house = line.rstrip().split(",")
    student = {"name":name, "house":house}
    students.append(student)

def get_name(student):
  return student["name"]

#can use "lambda student: student["name"] as an argument to pass a nameless function"
for student in sorted(students, key = get_name):
  print(f"{student['name']} is in {student['house']}")

#newer logic
students = []

#using the reader function from the csv module to help with the reading of the file
with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
      students.append({"name": row[0], "home": row[1]})

def get_name(student):
  return student["name"]

#can use "lambda student: student["name"] as an argument to pass a nameless function"
for student in sorted(students, key = get_name):
  print(f"{student['name']} is in {student['house']}")
