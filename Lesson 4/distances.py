distances = {
  "Voyayer 1": "163",
  "Voyayer 2": "136",
  "Pioneer 10": "80",
  "New Horizons": "58",
  "Pioneer 11": "44",
}

def main():
  spacecraft = input("Enter a spacecraft: ")

  #trying to handle multiple exceptions
  try:
    au = float(distances[spacecraft])
  
  #handling KeyError exception
  except KeyError:
    print(f"'{spacecraft}' is not in dictionary")
    return
  
  #habdling ValueError exception
  except ValueError:
    print(f"Can't convert '{distances[spacecraft]}' to a float")
    return

  m = convert(au)
  print(f"{m} m away")

def convert(au):
  return au * 149597870700

main()