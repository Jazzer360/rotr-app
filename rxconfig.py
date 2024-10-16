import os

import reflex as rx

redis = os.getenv('REDIS_URL')
print(f'Using REDIS_URL={redis}')

config = rx.Config(
    app_name="rotr_app",
    redis_url=os.getenv('REDIS_URL')
)
