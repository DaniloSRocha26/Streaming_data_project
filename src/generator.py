from faker import Faker
import random
fake = Faker()

usersList = []

plans = {
    "STANDARD_WITH_ADS": "7.99",
    "STANDARD": "17.99",
    "PREMIUM": "24.99"
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

    


    
def randomUserGenerator():
      for _ in range(1000):
        user_plan = random.choice(list(plans.keys()))
        user = {
            "name": fake.name(),
            "email": fake.email(),
            "age": random.randint(18,80),
            "country": fake.country(),
            "plan": random.choice(plans),
            "monthly_fee": plans[user_plan],
            "subscription_date": fake.date_between(start_date = '-1m')
            "watch_hours_per_month": random.randint(10, 70)
            
          }  
    



