from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

database = client["Streaming_Data"]
collection = database["users"]

collection.insert_one({"name": "Danilo", "age": 23})

print("user inserted")