import reflex as rx

from rotr_app.data.json_loader import load_food_data
from rotr_app.template import template

# Load food data from JSON
_food_data = load_food_data()
vendors = _food_data['vendors']


def menu_item(item: dict) -> rx.Component:
    if 'options' in item:
        options = [menu_option(option) for option in item.get('options', [])]
    else:
        options = None
    desc = item['desc'] if 'desc' in item else None
    return rx.box(
        rx.hstack(
            rx.cond(
                item.get('section'),
                rx.box(
                    rx.text(
                        item.get('section'),
                        size='3',
                        font_weight='bold',
                        text_decoration='underline'
                    ),
                    width='100%',
                    display='flex',
                    justify_content='center'
                ),
                rx.text(item.get('item'), size='3')
            ),
            rx.spacer(),
            rx.text(item.get('price'), size='3')
        ),
        rx.text(
            desc,
            size='2',
            margin_left='2em',
            font_style='italic'
        ),
        options,
        width='100%'
    )


def menu_option(option: dict) -> rx.Component:
    return rx.hstack(
        rx.spacer(),
        rx.text(option.get('option'), margin_left='1em'),
        rx.text(option.get('price')),
    )


def vendor_item(menu: dict) -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.card(
                rx.heading(
                    menu.get('vendor'),
                    align='center',
                    margin_top='.2em'
                ),
                rx.divider(margin_top='1em', margin_bottom='1em'),
                rx.vstack(
                    [menu_item(item) for item in menu.get('menu', [])]
                ),
                width='100%',
                padding='1.5em',
                padding_top='1em'
            ),
            align='center'
        ),
        size='1',
        padding='8px',
        width='100%'
    )


@rx.page(
    route='/food',
    title='Food Vendors')
@template
def food_page() -> rx.Component:
    return rx.box(
        [vendor_item(vendor) for vendor in vendors],
        width='100%',
        align='center'
    )
