from typing import Callable

import reflex as rx

from .components.navbar import navbar


def template(page: Callable[[], rx.Component]) -> rx.Component:
    def wrapper():
        return rx.vstack(
            navbar(),
            page(),
            align='center')
    return wrapper
