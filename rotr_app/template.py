from typing import Callable

import reflex as rx

from .components.navbar import navbar


def template(page: Callable[[], rx.Component]) -> rx.Component:
    return rx.vstack(
        navbar(),
        page())
