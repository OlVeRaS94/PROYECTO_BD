import requests
import json
from pymongo import MongoClient

# 1. Tu clave de API de TMDb
API_KEY = "a3c4c9034e1ff917ffbac6bb480bbc3c"
url = f"https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&with_genres=16&language=es-ES"

# 2. Petición a la API
response = requests.get(url)
data = response.json()

# 3. Guarda los datos en un archivo local (opcional)
with open("data/anime_tmdb.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# 4. Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["anime"]
coleccion = db["tmdb"]

# 5. Inserta los datos en MongoDB
if "results" in data:
    coleccion.insert_many(data["results"])
    print("Datos de TMDb guardados en MongoDB con éxito.")
else:
    print("No se encontraron resultados en la respuesta de la API.")
