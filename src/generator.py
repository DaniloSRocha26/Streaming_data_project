from faker import Faker
from datetime import timedelta
import random
fake = Faker()

usersList = []

plans = {
    "STANDARD_WITH_ADS": "7.99",
    "STANDARD": "17.99",
    "PREMIUM": "24.99"
}

genres = [
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

def churnUsers(subscription_date):
    is_Active_User = random.random()
    if is_Active_User <= 0.8:
        days_after = timedelta(days=random.randint(1, 30))
        return f"canceled on {subscription_date + days_after}"
    else:
        return "subscribed"



def randomUserGenerator():
      for _ in range(1000):
        user_plan = random.choice(list(plans.keys()))
        subscription_date = fake.date_between(start_date='-1m')
        user = {
            "name": fake.name(),
            "email": fake.email(),
            "age": random.randint(18,80),
            "country": fake.country(),
            "plan": user_plan,
            "monthly_fee": plans[user_plan],
            "subscription_date": str(subscription_date),
            "watch_hours_per_month": random.randint(10, 70),
            "is_active": churnUsers(subscription_date),
            "favorite_genre": random.choice(genres)
          }
        usersList.append(user)
    
randomUserGenerator()

for user in usersList:
    print(user)


