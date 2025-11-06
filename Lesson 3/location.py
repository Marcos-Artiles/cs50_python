#import a module from python
import sys

def main():

  coordinates_list = [42.376, -71.115]

  #tuple that allows to pack items
  coordinates = (42.376, -71.115)

  #print the size of bytes in memory
  print(f"{sys.getsizeof(coordinates_list)} bytes")
  print(f"{sys.getsizeof(coordinates)} bytes")

  #print the values
  print(f"Latitude: {coordinates[0]}")
  print(f"longtitude: {coordinates[1]}")

  #unpack the values
  latitude, longtitude = coordinates

  #print the values
  print(f"Latitude: {latitude}")
  print(f"longtitude: {longtitude}")

main()