#function main
def main():
    #get input from user
    number = int(input("Number: "))
    if is_even(number):
        print("The number is even")
    else:
        print("The number is odd")

#function that determines if a number is even or odd
def is_even(number):
    return number % 2 == 0
    
main()