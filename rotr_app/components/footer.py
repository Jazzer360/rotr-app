import datetime

import reflex as rx


def footer() -> rx.Component:
    now = datetime.datetime.now()
    date_str = now.strftime('%Y-%m-%d %H:%M')
    return rx.box(
        rx.container(
            rx.hstack(
                rx.text(
                    f'Last updated: {date_str}',
                    size='1',
                    color='gray',
                    padding_left='1em'
                ),
                rx.spacer(),
                rx.link(
                    "Privacy Notice",
                    href='/privacy.html',
                    text_align="right",
                    white_space="normal",
                    padding_right='1em',
                ),
                align="center",
                width="100%"
            ),
            size="1",
            padding_left='0px',
            padding_right='0px',
            padding_top='0px'
        ),
        width="100%"
    )
