from src.config import collection
import pandas as pd
import logging


def load_data():
    results = collection.find({})
    data = list(results)
    df = pd.DataFrame(data)
    logging.info(df.head())
    return df


def revenue_by_plan(df):
    result = df.groupby("plan")["monthly_fee"].sum()
    logging.info("\n" + str(result))
    return result


def revenue_by_genre(df):
    result = df.groupby("favorite_genre")["monthly_fee"].sum()
    logging.info("\n" + str(result))
    return result


def churn_by_plan(df):
    total_users = df.shape[0]
    logging.info(f"Total users: {total_users}")

    subscribed = df[df["is_active"] == True]
    subscribed_count = subscribed.shape[0]
    logging.info(f"Total subscribed users: {subscribed_count}")

    churned = df[df["is_active"] == False]
    churned_count = churned.shape[0]
    logging.info(f"Total churned users: {churned_count}")

    total_users_by_plan = df[df["is_active"] == True].groupby("plan")["_id"].count()
    logging.info(f"Total users by plan: {total_users_by_plan}")

    churned_count_by_plan = df[df["is_active"] == False].groupby("plan")["_id"].count()
    logging.info(f"Total churned users by plan: {churned_count_by_plan}")
    return total_users, subscribed_count, churned_count, total_users_by_plan, churned_count_by_plan


def age_distribution(df):
    bins = [17, 25, 35, 45, 54, 64, 81]
    labels = ["18-25", "26-35", "36-45", "46-54", "55-64", "65-80"]

    age_categories = pd.cut(df["age"], bins, labels=labels)
    users_per_age_group = age_categories.value_counts().sort_index()
    total_users = df.shape[0]

    logging.info(f"Total users: {total_users}")
    logging.info(f"Age distribution:\n{users_per_age_group}")

    return users_per_age_group, total_users


def avg_watch_hours_by_plan(df):
    avg_hours_per_plan = df.groupby("plan")["watch_hours_per_month"].mean()
    avg_hours_per_plan_formatted = avg_hours_per_plan.round(1)
    logging.info("Average watch hours per plan:")
    logging.info(f"\n{avg_hours_per_plan_formatted}")
    return avg_hours_per_plan_formatted
