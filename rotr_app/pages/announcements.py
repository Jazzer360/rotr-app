import reflex as rx

from ..template import template
from ..components.navbar import NavState
from ..data.firestore import Announcement


def make_card(data: Announcement):
    return rx.card(
            rx.vstack(
                rx.hstack(
                    rx.heading(data.user),
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
                rx.text(f'"{data.message}"', font_style='italic'),
                width='100%'
            ),
            width='100%'
        )


@rx.page(route='/announcements', title="Announcements")
@template
def announcements():
    return rx.box(
        rx.container(
            rx.vstack(
                rx.foreach(NavState.announcements, make_card),
                width='100%'
            ),
            padding_top='0px',
            size='2'
        ),
        width='100%'
    )
