import reflex as rx

from ..components.navbar import NavState
from ..template import template


vendors = [
    {
        'vendor': 'Cup \'N Saucer',
        'menu': [
            {
                'item': 'More Info to Come',
                'desc': 'TBA'
            }
        ]
    },
    {
        'vendor': 'Cheese Carriage',
        'menu': [
            {
                'item': 'Cheese Curds'
            }
        ]
    }
]


def menu_item(item: dict) -> rx.Component:
    return [
        rx.text(item.get('item'), size='3'),
        rx.text(
            item.get('desc'),
            size='2',
            margin_left='2em',
            font_style='italic'
        )
    ]


def vendor_item(menu: dict) -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading(menu.get('vendor')),
            rx.card(
                rx.vstack(
                    [menu_item(item) for item in menu.get('menu')]
                ),
                width='100%'
            ),
            align='center'
        ),
        size='1',
        padding='8px'
    )


@rx.page(
    route='/food',
    title='Food Vendors',
    on_load=NavState.update)
@template
def schedule() -> rx.Component:
    return rx.vstack(
        [rx.box(vendor_item(vendor), width='100%') for vendor in vendors],
        width='100%',
        align='center'
    )
