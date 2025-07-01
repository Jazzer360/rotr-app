import os

import reflex as rx


config = rx.Config(
    app_name="rotr_app",
    redis_url=os.getenv('REDIS_URL'),
    plugins=[rx.plugins.TailwindV3Plugin()],
    show_built_with_reflex=False
)
