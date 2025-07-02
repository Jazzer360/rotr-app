from typing import Callable

import reflex as rx

from rotr_app.components import footer, navbar, survey_popup
from rotr_app.components.surveypopup import SurveyState


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
