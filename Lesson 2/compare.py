#logic operators: "<", ">", "<=", ">=", "==", "!=" 

#get input from user
x = int(input("What's X?: "))
y = int(input("What's X?: "))

#using if && elif for compararing and else for assuming
if x < y:
    print("X is less than Y.")
elif x > y:
    print("X is greater than Y.")
else:
    print("X is equal to Y.")

#using "or" tu evaluate if at least one condition is met
if x < y or x > y:
    print("X is no equal to Y.")
else:
    print("X is equal to Y.")
