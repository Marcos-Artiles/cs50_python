#importing the method sample from soil
from soil import sample

#main function
def main():
  moisture = sample()
  days = 0
  print(f"Day: {days} Moisture is {moisture}%")

  #while loop that will iterate until the condition is met
  while moisture > 20:
    moisture = sample()
    days += 1
    print(f"Day: {days} Moisture is {moisture}%")
  
  print("Time to water!")

main()