from src.config import collection
import logging
from pymongo.errors import PyMongoError



def insert_users(users_list):
    try:
        if not users_list:
            logging.warning("insert_users called with empty list")
        else:
            result = collection.insert_many(users_list)
            logging.info(f"{len(result.inserted_ids)} users inserted")
    except PyMongoError:
        logging.error("Failed to insert users")     
        raise      
            


def clear_collection():
    try: 
        collection.delete_many({})
        logging.info("All users deleted")
    except PyMongoError:
        logging.error("Failed to Delet users")
        raise

def get_all_users():
        return list(collection.find())

