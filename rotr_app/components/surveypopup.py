from datetime import date

import reflex as rx

from ..util.utils import date_from_day
from .navbar import links


class SurveyState(rx.State):
    survey_clicked: str = rx.Cookie(
        name="survey_clicked", max_age=60 * 60 * 24 * 7)
    visit_count: str = rx.Cookie(
        name="visit_count", max_age=60 * 60 * 24 * 7)
    show_popup: bool = False

    @rx.event
    def check_survey_status(self):
        if self.survey_clicked == "T":
            if date.today().isoformat() < date_from_day("F"):
                self.survey_clicked = "F"
            self.show_popup = False
            return

        if date.today().isoformat() < date_from_day("F"):
            self.show_popup = False
            return

        try:
            visits = int(self.visit_count[1:])
        except (ValueError, TypeError):
            visits = 0

        if visits == 0:
            self.visit_count = "v1"
            self.show_popup = False
        else:
            self.visit_count = "v" + str(visits + 1)
            if visits > 0 and (visits + 1) % 3 == 0:
                self.show_popup = True
            else:
                self.show_popup = False

    @rx.event
    def mark_survey_clicked(self):
        self.survey_clicked = "T"
        self.show_popup = False

    @rx.event
    def close_popup(self):
        self.show_popup = False


def survey_popup():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Help Us Improve!"),
            rx.dialog.description(
                "We'd love to get your feedback. "
                "Would you be willing to take a short survey?"
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "No thanks",
                        on_click=SurveyState.close_popup,
                        variant="soft",
                        color_scheme="gray",
                    ),
                ),
                rx.link(
                    rx.button(
                        "Take Survey",
                        on_click=SurveyState.mark_survey_clicked,
                    ),
                    href=links['Survey'],
                    is_external=True,
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
                flex_wrap="wrap",
            ),
        ),
        open=SurveyState.show_popup,
    )
