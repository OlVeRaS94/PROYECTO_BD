import requests
import json
from pymongo import MongoClient

# 1. Consulta SPARQL a Wikidata
query = """
SELECT ?anime ?animeLabel ?fecha ?autorLabel WHERE {
  ?anime wdt:P31 wd:Q5398426.
  OPTIONAL { ?anime wdt:P577 ?fecha. }
  OPTIONAL { ?anime wdt:P50 ?autor. }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],es". }
}
LIMIT 50
"""

url = "https://query.wikidata.org/sparql"
headers = {"Accept": "application/sparql-results+json"}
params = {"query": query}

# 2. Hacemos la petición
response = requests.get(url, params=params, headers=headers)
data = response.json()

# 3. Guardamos localmente (opcional)
with open("data/anime_wikidata.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# 4. Procesamos para MongoDB
documentos = data["results"]["bindings"]

# 5. Insertamos en MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["anime"]
coleccion = db["wikidata"]
coleccion.insert_many(documentos)

print("Datos de Wikidata insertados en MongoDB con éxito.")
