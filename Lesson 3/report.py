#defining main function
def main():
  spacecraft = {"name": "Voyayer 1", "distance": 163}
  spacecraft.update({"orbit": "Sun"})
  print(create_report(spacecraft))

#defining a function that will emmit a report
#using .get to obtain a key, if there is none, will return a default value
def create_report(spacecraft):
  return f"""
  ===== REPORT =====
  
  Name: {spacecraft["name"]}
  Distance: {spacecraft.get("distance", "Unknown")} AU
  Orbit:{spacecraft.get("orbit", "Unknown")}

  ==================
  """

main()