import requests

def main():

  print("Search the Art Institute of Chicago")
  artist = input("Artist: ")

  try:
    #doing a get request to an api with additional query as context
    response = requests.get(
      "https://api.artic.edu/api/v1/artworks/search",
      {"q": artist}
    )
    #confirming that the action was executed
    response.raise_for_status()

  #rasing an httpError if the action failed
  except requests.HTTPError:
    print("Couldn't complete request")
    return
  
  content = response.json()
  for artwork in content["data"]:
    print(f"* {artwork['title']}")

main()