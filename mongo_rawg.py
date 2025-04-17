import requests
import json
from pymongo import MongoClient

# 1. Tu clave de API de RAWG
API_KEY = "ff06ca10089b47e5aa9c2682121ac03b"
url = f"https://api.rawg.io/api/games?key={API_KEY}"

# 2. Petición a la API
response = requests.get(url)
data = response.json()

# 3. Guarda los datos en archivo local (opcional)
with open("data/juegos_rawg.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

# 4. Conecta con MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["videojuegos"]
coleccion = db["juegos_rawg"]

# 5. Inserta los resultados en la base de datos
coleccion.insert_many(data["results"])

print("Datos de RAWG guardados en MongoDB con éxito.")
