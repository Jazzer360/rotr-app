import reflex as rx

from rotr_app.data.json_loader import load_bar_data
from rotr_app.template import template

# Load bar data from JSON
_bar_data = load_bar_data()
vendor_name = _bar_data['vendor']
items = _bar_data['items']


def bar_selection(selection: dict) -> rx.Component:
    return rx.box(
        rx.text(
            selection.get('name'),
            size='2',
            font_weight='bold',
            margin_left='2em',
            padding_top='1em',
        ),
        rx.text(
            selection.get('description'),
            size='2',
            margin_left='3em',
            font_style='italic'
        ),
        width='100%'
    )


def bar_item(item: dict) -> rx.Component:
    selections = [
        bar_selection(selection)
        for selection in item.get('selection', [])
    ]
    return rx.box(
        rx.hstack(
            rx.text(item.get('item'), size='3'),
            rx.spacer(),
            rx.text(item.get('price'), size='3')
        ),
        *selections,
        width='100%'
    )


def bar_vendor() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.card(
                rx.heading(
                    vendor_name,
                    margin_bottom='.5em',
                    padding_top='.2em',
                    align='center'
                ),
                rx.text(
                    'To cut down on waste, we would appreciate if you either '
                    'bring your own cup or purchase one at the merch tent. '
                    'Cups are $15, or you can get a cup, koozie, and drink '
                    'for $25.',
                    size='2',
                    font_style='italic',
                    margin_bottom='1em'
                ),
                rx.divider(margin_top='1em', margin_bottom='1em'),
                rx.vstack(
                    [bar_item(item) for item in items],
                    padding_bottom='.2em'
                ),
                padding='1.5em',
                padding_top='1em',
                width='100%'
            ),
            align='center'
        ),
        size='1',
        padding='8px',
        width='100%'
    )


@rx.page(
    route='/bar',
    title='Bar')
@template
def bar_page() -> rx.Component:
    return rx.box(
        bar_vendor(),
        width='100%',
        align='center'
    )
