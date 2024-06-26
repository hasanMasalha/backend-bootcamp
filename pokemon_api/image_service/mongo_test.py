from pymongo import MongoClient
from gridfs import GridFS
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
print("helllllo")
# Connect to MongoDB
try:
    logger.info("Attempting to connect to MongoDB at localhost:27017")
    client = MongoClient("mongodb://localhost:27017/")
    db = client.pokemon_images
    fs = GridFS(db)
    logger.info("Connected to MongoDB successfully")
    # Try an operation to ensure everything is working
    test_file_id = fs.put(b"test", filename="test.txt")
    logger.info(f"Uploaded test file with ID: {test_file_id}")
except Exception as e:
    logger.error(f"Error connecting to MongoDB: {e}")
