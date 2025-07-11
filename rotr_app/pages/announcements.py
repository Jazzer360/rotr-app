import reflex as rx

from rotr_app.template import template
from rotr_app.components.navbar import NavState, Announcement


def make_card(data: Announcement) -> rx.Component:
    return rx.card(
            rx.vstack(
                rx.hstack(
                    rx.heading(data.subject),
                    rx.spacer(),
                    rx.badge(
                        rx.moment(
                            data.time * 1000,
                            from_now_during=1000*60*60*24,
                            format='ddd h:mma'
                        )
                    ),
                    width='100%'
                ),
                rx.foreach(data.message, message_paragraph),
                rx.box(
                    rx.text(f'- {data.user}', align='right'),
                    padding_right='1em',
                    width='100%'
                ),
                width='100%'
            ),
            width='100%'
        )


def message_paragraph(txt: str) -> rx.Component:
    return rx.text(txt, font_style='italic')


@rx.page(
    route='/announcements',
    title='Announcements',
    on_load=NavState.set_read)
@template
def announcements():
    return rx.box(
        rx.container(
            rx.vstack(
                rx.foreach(NavState.announcements, make_card),
                width='100%'
            ),
            padding_top='8px',
            size='2'
        ),
        width='100%'
    )
