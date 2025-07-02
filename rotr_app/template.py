from typing import Callable

import reflex as rx

from rotr_app.components import footer, navbar, survey_popup


def template(page: Callable[[], rx.Component]) -> Callable[[], rx.Component]:
    def wrapper():
        return rx.vstack(
            navbar(),
            page(),
            footer(),
            survey_popup(),
            align='center'
        )

    return wrapper
