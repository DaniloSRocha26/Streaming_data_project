from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Connects to MongoDB using MONGO_URI
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)


database = client["Streaming_Data"]
collection = database["users"]
