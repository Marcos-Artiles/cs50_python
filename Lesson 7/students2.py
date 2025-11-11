import csv

students = []

#using DictReader function from the csv module to help with the reading of the file with no regard for the current order of the data
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
      students.append({"name": row[0], "home": row[1]})

def get_name(student):
  return student["name"]

#can use "lambda student: student["name"] as an argument to pass a nameless function"
for student in sorted(students, key = get_name):
  print(f"{student['name']} is in {student['house']}")

name = input("What's your name?: ")
home = input("What's your home?: ")

with open("students.csv", "a") as file:
   writer = csv.DictWriter(file, fieldnames=["name", "home"])
   writer.writerow({"name": name, "home": home})
