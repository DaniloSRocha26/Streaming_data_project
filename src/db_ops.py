from src.config import collection
import logging
def insert_users(users_list):
    if not users_list:
        logging.warning("insert_users called with empty list")
    else:
        result = collection.insert_many(users_list) 
        logging.info(f"{len(result.inserted_ids)}, users inserted")    
        
        
        
def clear_collection():
     collection.delete_many({})
     logging.info("All users deleted")
        
