def main():
  pace = get_pace(miles = 26.2, minutes = 180)
  print(f"You need to run each mile in {round(pace, 2)} minutes.")

def get_pace(miles, minutes):

  if not minutes > 0:

    #raising a customized exception/error
    raise ValueError(f"Invalid value '{minutes}' for minutes.")
  
  return minutes / miles

main()