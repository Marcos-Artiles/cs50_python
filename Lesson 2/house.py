#get input from user
name = int(input("Name: "))

#function match for hardcoded handlings
match name:
    case "Harry"| "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")