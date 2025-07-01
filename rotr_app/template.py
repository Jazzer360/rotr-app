from typing import Callable

import reflex as rx

from .components import navbar, footer, survey_popup
from .components.surveypopup import SurveyState


def template(page: Callable[[], rx.Component]) -> Callable[[], rx.Component]:
    def wrapper():
        return rx.vstack(
            navbar(),
            page(),
            footer(),
            survey_popup(),
            align='center',
            on_mount=SurveyState.check_survey_status,
        )

    return wrapper
