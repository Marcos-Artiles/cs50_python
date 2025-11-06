#declaring a dictionare
distances = {
  "Voyayer 1": 163,
  "Voyayer 2": 136,
  "Pioneer 10": 80,
  "New Horizons": 58,
  "Pioneer 11": 44,
}

#defining the main function
#using .keys and .values to iterate on a dictionary
def main():
  for name in distances.keys():
    print(f"{name} is {distances[name]} AU from Earth")
  
  for distance in distances.values():
    print(f"{distance} AU is {convert(distance)} m")


def convert(au):
  return au * 149597870700

main()