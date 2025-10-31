#Ask user for their name
name = input("What's your name?: ")

#capitalize the user's name
#name = name.capitalize()

#capitalize the user's name and last name
#name = name.title()

#split string into multiple strings
#first, last = name.split(" ")

#concatenate methods
name = name.strip().title()

# Say hello to user
print ("Hello, " + name)

#other form to assign parameters
print ("Hello,",name)

#Overide "end" parameter
print ("Hello, ", end="")
print (name)

#couts inside of couts
print ('Hello, "friend" ')

#format string
print (f"Hello, {name}")

