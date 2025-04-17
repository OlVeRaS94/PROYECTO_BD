import requests
import json

API_KEY = "a3c4c9034e1ff917ffbac6bb480bbc3c"
url = f"https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&with_genres=16&language=es-ES"

response = requests.get(url)
data = response.json()

with open("data/anime_tmdb.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Datos de anime guardados con éxito desde TMDb.")
