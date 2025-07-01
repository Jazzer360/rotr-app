from typing import Callable

import reflex as rx

from .components.navbar import navbar
from .components.footer import footer


def template(page: Callable[[], rx.Component]) -> Callable[[], rx.Component]:
    def wrapper():
        return rx.vstack(
            navbar(),
            page(),
            footer(),
            align='center')
    return wrapper
