import logging
import os
import sys
from pymongo.errors import PyMongoError
from datetime import datetime
from src.generator import random_users_generator
from src.db_ops import insert_users, clear_collection
from src.analysis import revenue_by_plan, revenue_by_genre, churn_by_plan, load_data, age_distribution, avg_watch_hours_by_plan




logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(levelname)s: %(message)s (%(filename)s: %(lineno)d)"
)

logger = logging.getLogger("DevApp")


if __name__ == "__main__":
    try:
        logger.info("Starting data pipeline")
        
        now = datetime.now()
        
        ct = now.strftime("%m-%d-%Y_%H-%M-%S")
        logger.info(f"current time:, {ct}")

        clear_collection()
        users_list = random_users_generator(10000)
        insert_users(users_list)

        
        df = load_data()
        logging.info(df.columns)
        
        path = os.path.join(f"reports", "data_" + ct + ".csv")
        df.to_csv(path, index=False, encoding="utf-8")
        logger.info(f"CSV saved in: {path}")
        
        result_revenue_by_plan = revenue_by_plan(df)
        path = os.path.join(f"reports", "revenue_by_plan" + ct + ".csv")
        result_revenue_by_plan.to_csv(path, index=False, encoding = "utf-8")
        
        
        result_revenue_by_genre = revenue_by_genre(df)
        path = os.path.join(f"reports", "revenue_by_genre" + ct + ".csv")
        result_revenue_by_genre.to_csv(path, index=False, encoding = "utf-8")
        
        
        result_total, subscribed, churned, total_users_by_plan, churned_by_plan = churn_by_plan(df) 
        path = os.path.join(f"reports", "churned_by_plan" + ct + ".csv")
        churned_by_plan.to_csv(path, index=False, encoding = "utf-8")
    
        path = os.path.join(f"reports", "total_users_by_plan" + ct + ".csv")
        total_users_by_plan.to_csv(path, index=False, encoding="utf-8")
    
        
        
        result_users_per_age_group, total_users = age_distribution(df)
        path = os.path.join(f"reports", "users_per_age_group" + ct + ".csv")
        result_users_per_age_group.to_csv(path, index=False, encoding = "utf-8")
        
        
        
        
        result_avg_watch_hours_by_plan = avg_watch_hours_by_plan(df)
        path = os.path.join(f"reports", "avg_watch_hours_by_plan" + ct + ".csv")
        result_avg_watch_hours_by_plan.to_csv(path, index=False, encoding = "utf-8")
        
        

        logger.info("Pipeline complete")
    except PyMongoError:
        logging.error("Pipeline failed due to database error")
        raise
    except Exception:
        logging.error("Pipeline failed due to unexpected error")
        raise
    