import requests

def get_artworks(query, limit):

  try:
    #doing a get request to an api with additional query as context
    response = requests.get(
      "https://api.artic.edu/api/v1/artworks/search",
      {"q": query, "limit": limit}
    )
    #confirming that the action was executed
    response.raise_for_status()
     
  except requests.HTTPError:
    return []
  
  content = response.json()
  return [artwork["title"] for artwork in content["data"]]