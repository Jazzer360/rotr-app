import os

import reflex as rx


config = rx.Config(
    app_name="rotr_app",
    api_url=os.getenv('API_URL', 'http://localhost:8000'),
    redis_url=os.getenv('REDIS_URL'),
    show_built_with_reflex=False
)
