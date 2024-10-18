print('loading config')
import os

import reflex as rx


config = rx.Config(
    app_name="rotr_app",
    redis_url=os.getenv('REDIS_URL'),
    loglevel='debug'
)

print('config loaded')