from pymongo import MongoClient
import logging
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
import os


# Connects to MongoDB using MONGO_URI
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
if mongo_uri == None:
    raise EnvironmentError("mongo_uri is None")

try:
    client = MongoClient(mongo_uri)
except ConnectionFailure:
    logging.error("Error to connect to client")
    raise


database = client["Streaming_Data"]
collection = database["users"]
