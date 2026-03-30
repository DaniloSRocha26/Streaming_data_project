import logging
import os
import sys
from src.generator import random_users_generator
from src.db_ops import insert_users, clear_collection
from src.analysis import revenue_by_plan, revenue_by_genre, churn_by_plan, load_data, age_distribuition, avg_watch_hours_by_plan


logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(levelname)s: %(message)s (%(filename)s: %(lineno)d)"
)

logger = logging.getLogger("DevApp")


if __name__ == "__main__":
    logger.info("Starting data pipeline")

    clear_collection()
    users_list = random_users_generator(1000)
    insert_users(users_list)

    df = load_data()
    logging.info(df.columns)
    
    path = os.path.join("reports", "data.csv")
    df.to_csv(path, index=False, encoding="utf-8")
    logger.info(f"CSV saved in: {path}")
    
    revenue_by_plan(df)
    revenue_by_genre(df)
    churn_by_plan(df)
    age_distribuition(df)
    avg_watch_hours_by_plan(df)

    logger.info("Pipeline complete")
    

    