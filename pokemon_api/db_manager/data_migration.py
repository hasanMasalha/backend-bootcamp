import pymysql
import json
import requests
from pymongo import MongoClient, GridFS

# Load data from JSON file
with open('pokemons.json', 'r') as file:
    data = json.load(file)

# MySQL setup
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='pokemon_db'
    )

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client.pokemon_images
fs = GridFS(db)

# Fetch correct types using external API
def fetch_pokemon_types(name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
    if response.status_code == 200:
        return [type_info['type']['name'] for type_info in response.json()['types']]
    return []

# Insert data into database
def migrate_data():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        for pokemon in data:
            # Insert trainers and ownership
            for trainer in pokemon['ownedBy']:
                cursor.execute(
                    "INSERT INTO trainers (name, town) VALUES (%s, %s) ON DUPLICATE KEY UPDATE id=id",
                    (trainer['name'], trainer['town'])
                )
                cursor.execute("SELECT id FROM trainers WHERE name=%s", (trainer['name'],))
                trainer_id = cursor.fetchone()[0]

                # Insert pokemon
                pokemon_types = fetch_pokemon_types(pokemon['name'])
                for poke_type in pokemon_types:
                    cursor.execute(
                        "INSERT INTO pokemons (name, type, height, weight) VALUES (%s, %s, %s, %s)",
                        (pokemon['name'], poke_type, pokemon['height'], pokemon['weight'])
                    )
                    pokemon_id = cursor.lastrowid

                    # Insert ownership
                    cursor.execute(
                        "INSERT INTO pokemon_ownership (pokemon_id, trainer_id) VALUES (%s, %s)",
                        (pokemon_id, trainer_id)
                    )

                # Insert image into MongoDB
                image_response = requests.get(f"https://pokeapi.co/api/v2/pokemon-form/{pokemon['id']}/")
                image_url = image_response.json()['sprites']['front_default']
                image_data = requests.get(image_url).content
                file_id = fs.put(image_data, filename=f"{pokemon['name']}.png")
                print(f"Uploaded image for {pokemon['name']} with file id {file_id}")

        connection.commit()
    connection.close()

if __name__ == "__main__":
    migrate_data()
