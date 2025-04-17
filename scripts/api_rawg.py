import requests
import json

API_KEY = "ff06ca10089b47e5aa9c2682121ac03b"
url = f"https://api.rawg.io/api/games?key={API_KEY}"

response = requests.get(url)
data = response.json()

with open("data/juegos_rawg.json", "w") as f:
    json.dump(data, f, indent=4)

print("Datos guardados con éxito.")
