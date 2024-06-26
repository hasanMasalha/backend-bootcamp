import json
import requests
from pymongo import MongoClient
from gridfs import GridFS
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)  # Set to DEBUG to catch more details
logger = logging.getLogger(__name__)

# Load data from JSON file
try:
    with open('C:/Users/hasan/backend-bootcamp/backend-bootcamp/pokemon_api/db_manager/pokemons_data.json', 'r') as file:
        data = json.load(file)
    logger.info("Loaded data from pokemons.json")
except FileNotFoundError:
    logger.error("pokemons.json file not found")
    raise
except Exception as e:
    
    logger.error(f"Unexpected error loading JSON: {e}")
    raise

# MongoDB setup
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client.pokemon_images
    fs = GridFS(db)
    logger.info("Connected to MongoDB successfully")
except Exception as e:
    logger.error(f"Error connecting to MongoDB: {e}")
    raise

# Insert data into MongoDB
def migrate_data():
    logger.info("Starting data migration...")
    for pokemon in data:
        try:
            logger.debug(f"Processing Pokémon: {pokemon['name']}")
            # Fetch image URL from Pokémon API
            image_response = requests.get(f"https://pokeapi.co/api/v2/pokemon-form/{pokemon['id']}/")
            if image_response.status_code == 200:
                image_url = image_response.json()['sprites']['front_default']
                if image_url:
                    # Download image
                    image_data = requests.get(image_url).content
                    # Upload image to MongoDB GridFS
                    file_id = fs.put(image_data, filename=f"{pokemon['name']}.png")
                    logger.info(f"Uploaded image for {pokemon['name']} with file id {file_id}")
                else:
                    logger.warning(f"No image URL found for {pokemon['name']}")
            else:
                logger.error(f"Failed to fetch image URL for {pokemon['name']}, status code: {image_response.status_code}")
        except Exception as e:
            logger.error(f"Error processing Pokémon {pokemon['name']}: {e}")
    logger.info("Data migration completed.")

if __name__ == "__main__":
    try:
        migrate_data()
    except Exception as e:
        logger.error(f"Data migration failed: {e}")
