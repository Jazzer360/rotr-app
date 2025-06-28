import reflex as rx

from ..components.navbar import NavState
from ..template import template


vendors = [
    {
        'vendor': 'Cheese Carriage',
        'menu': [
            {
                'item': 'Cheese Curds',
                'price': '$8'
            },
            {
                'item': 'Corn Dog',
                'price': '$6'
            },
            {
                'item': 'Pop & Water',
                'price': '$3'
            }
        ]
    },
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
        'vendor': "Ole's Gathering Place",
        'menu': [
            {
                'item': 'Smoked Pork Sandwich',
                'price': '$8',
                'options': [
                    {
                        'option': 'w/ coleslaw, smoked baked beans',
                        'price': '$12'
                    }
                ]
            },
            {
                'item': 'Smoked Brisket Sandwich',
                'price': '$10',
                'options': [
                    {
                        'option': 'w/ coleslaw, smoked baked beans',
                        'price': '$14'
                    }
                ]
            },
            {
                'item': 'Queso Bacon Mac and Cheese',
                'price': '$10',
                'options': [
                    {
                        'option': 'w/ pork',
                        'price': '$12'
                    },
                    {
                        'option': 'w/ brisket',
                        'price': '$14'
                    }
                ]
            },
            {
                'item': 'Queso Nachos (onion, tomato, jalapeno)',
                'price': '$10',
                'options': [
                    {
                        'option': 'w/ pork',
                        'price': '$12'
                    },
                    {
                        'option': 'w/ brisket',
                        'price': '$14'
                    }
                ]
            },
            {
                'item': 'Oledelphia (pork)',
                'price': '$12'
            },
            {
                'item': 'Oledelphia (brisket)',
                'price': '$14',
                'options': [
                    {
                        'option': 'w/ coleslaw, smoked baked beans',
                        'price': '$16'
                    }
                ]
            },
            {
                'item': 'Side of colelsaw, smoked baked beans',
                'price': '$3'
            },
            {
                'item': 'Pepsi, Mt. Dew, Dr. Pepper, Diet Dr. Pepper',
                'price': '$1'
            }
        ]
    }
]


def menu_item(item: dict) -> rx.Component:
    if 'options' in item:
        options = [menu_option(option) for option in item.get('options')]
    else:
        options = None
    desc = item['desc'] if 'desc' in item else None
    return rx.box(
        rx.hstack(
            rx.text(item.get('item'), size='3'),
            rx.spacer(),
            rx.text(item.get('price'), size='3')
        ),
        options,
        rx.text(
            desc,
            size='2',
            margin_left='2em',
            font_style='italic'
        ),
        width='100%'
    )


def menu_option(option: dict):
    return rx.hstack(
        rx.text(option.get('option'), margin_left='1em'),
        rx.spacer(),
        rx.text(option.get('price'))        
    )


def vendor_item(menu: dict) -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.card(
                rx.heading(menu.get('vendor'), margin_bottom='1em'),
                rx.vstack(
                    [menu_item(item) for item in menu.get('menu')]
                ),
                width='100%'
            ),
            align='center'
        ),
        size='1',
        padding='8px',
        width='100%'
    )


@rx.page(
    route='/food',
    title='Food Vendors',
    on_load=NavState.update)
@template
def schedule() -> rx.Component:
    return rx.box(
        [vendor_item(vendor) for vendor in vendors],
        width='100%',
        align='center'
    )
