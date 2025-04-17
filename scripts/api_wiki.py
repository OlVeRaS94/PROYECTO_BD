import requests
import json

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

response = requests.get(url, params={"query": query}, headers=headers)
data = response.json()

with open("data/anime_wikidata.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Datos de anime guardados con éxito desde Wikidata.")
