import json
import requests
import sys

if len(sys.argv) != 2:
  sys.exit()

#get a json file from itunes
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

#print the json file indented, making it easy to read
print(json.dumps(response.json()), indent= 2)

o = response.json()
for result in o["results"]:
  print(result["trackName"])