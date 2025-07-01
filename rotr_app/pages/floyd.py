import reflex as rx

from rotr_app.template import template
from rotr_app.data.firestore import get_manager


class FloydState(rx.State):
    logged_in: bool = False
    user: str = ''
    subject: str = ''
    message: str = ''
    loading: bool = False

    @rx.event
    def login(self, form_data: dict):
        self.loading = True
        yield
        user = form_data.get('user')
        pw = form_data.get('password')
        if user and pw and get_manager().validate_user(user, pw):
            self.user = user
            self.logged_in = True
        else:
            yield rx.toast.error('Nice try...')
        self.loading = False

    @rx.event
    def make_post(self, form_data: dict):
        self.loading = True
        yield
        message = form_data.get('message')
        subject = form_data.get('subject')
        if message:
            get_manager().save_post(
                user=self.user, subject=subject, message=message)
            self.message = ''
            self.subject = ''
            yield rx.toast.success('The masses have been notified!')
        self.loading = False

    @rx.event
    def set_subject(self, value: str):
        self.subject = value

    @rx.event
    def set_message(self, value: str):
        self.message = value


def login() -> rx.Component:
    return rx.card(
        rx.form(
            rx.vstack(
                rx.center(
                    rx.heading(
                        "Sign in",
                        size="6",
                        as_="h2",
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Who is this?",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("user")),
                        placeholder="Probably not Floyd",
                        name='user',
                        type="text",
                        size="3",
                        width="100%",
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "What's the password?",
                            size="3",
                            weight="medium",
                        ),
                        justify="between",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        placeholder="Probably your pet",
                        name='password',
                        type="password",
                        size="3",
                        width="100%",
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.button("Sign in", type='submit', size="3", width="100%",
                          loading=FloydState.loading),
                spacing="6",
                width="100%",
            ),
            on_submit=FloydState.login
        ),
        max_width="28em",
        size="4",
        width="100%",
    )


def post_form() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="megaphone", size=32),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Make an announcement",
                        size="4",
                        weight="bold",
                    ),
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    rx.flex(
                        rx.text(
                            "Subject",
                            style={
                                "fontSize": "15px",
                                "fontWeight": "500",
                                "lineHeight": "35px",
                            },
                        ),
                        rx.input(
                            value=FloydState.subject,
                            placeholder="The deets.",
                            name='subject',
                            type="text",
                            size="3",
                            width="100%",
                            on_change=FloydState.set_subject
                        ),
                        rx.text(
                            "Message",
                            style={
                                "fontSize": "15px",
                                "fontWeight": "500",
                                "lineHeight": "35px",
                            },
                        ),
                        rx.text_area(
                            value=FloydState.message,
                            placeholder="Spread the good gospel of Floyd here",
                            name="message",
                            resize="vertical",
                            on_change=FloydState.set_message,
                            height="250px"
                        ),
                        direction="column",
                        spacing="1",
                    ),
                    rx.form.submit(
                        rx.button("Submit", loading=FloydState.loading),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=FloydState.make_post,
                reset_on_submit=False,
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
    )


@rx.page(route='/floyd', title="Floyd's Happy Place")
@template
def floyd():
    return rx.cond(
        FloydState.logged_in,
        post_form(),
        login()
    )
