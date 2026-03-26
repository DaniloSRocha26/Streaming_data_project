from faker import Faker
from datetime import timedelta
import random
fake = Faker()

PLANS = {
    "STANDARD_WITH_ADS": 7.99,
    "STANDARD": 17.99,
    "PREMIUM": 24.99
}

GENRES = [
    "Action",
    "Comedy",
    "Drama",
    "Horror",
    "Romance",
    "Sci-Fi",
    "Thriller",
    "Fantasy",
    "Documentary",
    "Animation"
]

def churn_users(subscription_date):
    is_active_user = random.random()
    if is_active_user <= 0.2:
        days_after = timedelta(days=random.randint(1, 30))
        return False, subscription_date + days_after
    else:
        return True, None

    

def generate_user():
    subscription_date = fake.date_between(start_date='-1m')    
    is_active, cancel_date = churn_users(subscription_date)    
    user_plan = random.choice(list(PLANS.keys()))
    user = {
        "name": fake.name(),
        "email": fake.email(),
        "age": random.randint(18,80),
        "country": fake.country(),
        "plan": user_plan,
        "monthly_fee": PLANS[user_plan],
        "subscription_date": str(subscription_date),
        "watch_hours_per_month": random.randint(10, 70),
        "is_active": is_active,
        "cancel_date": str(cancel_date) if cancel_date else None,
        "favorite_genre": random.choice(GENRES)
        }
    return user
    
def random_users_generator(n):
    return[generate_user() for _ in range(n)]

users_list = random_users_generator(1000)
