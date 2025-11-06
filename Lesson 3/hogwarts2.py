#declaring a dictionary
students = {
  "Hermione": "Gryffindor",
  "Harry": "Gryffindor",
  "Ron" : "Gryffindor",
  "Draco": "Slytherin",
}

#printing the value assosiated with the key provided
print(students["Hermione"])

#printing the key + the value overriding the separator with an arrow
for student in students:
  print(student, students[student], sep= " -> ")

#declaring a list of dictionaries
students = [
  {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
  {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
  {"name": "Ron", "house": "Gryffindor", "patronus": "Jack"},
  {"name": "Draco", "house": "Slytherin", "patronus": None},
]

#printing the values assosiated with the keys and overriding the separator with an arrow
for student in students:
  print(student["name"], student["house"], student["patronus"], sep= " -> ")