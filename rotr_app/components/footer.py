import datetime
import pytz

import reflex as rx


def footer() -> rx.Component:
    central = pytz.timezone('America/Chicago')
    now = datetime.datetime.now(central)
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
                    'Privacy Notice',
                    href=(
                        'https://storage.googleapis.com/rotr-app-assets/'
                        'privacy.html'
                    ),
                    text_align='right',
                    white_space='normal',
                    padding_right='1em',
                    is_external=True
                ),
                align='center',
                width='100%'
            ),
            size='1',
            padding_left='0px',
            padding_right='0px',
            padding_top='0px'
        ),
        width='100%'
    )
