import reflex as rx

from rotr_app.components.navbar import NavState
from rotr_app.data.json_loader import load_bar_data
from rotr_app.template import template

# Load bar data from JSON
_bar_data = load_bar_data()
vendor_name = _bar_data['vendor']
items = _bar_data['items']


def bar_selection(selection: dict) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(selection.get('name'), size='2', font_weight='bold', margin_left='2em'),
            rx.spacer(),
        ),
        rx.text(
            selection.get('description'),
            size='2',
            margin_left='3em',
            font_style='italic'
        ) if selection.get('description') else None,
        width='100%'
    )


def bar_item(item: dict) -> rx.Component:
    selections = [bar_selection(selection) for selection in item.get('selection', [])]
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
                rx.heading(vendor_name, margin_bottom='1em'),
                rx.vstack(
                    [bar_item(item) for item in items]
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
    route='/bar',
    title='Bar',
    on_load=NavState.update)
@template
def bar_page() -> rx.Component:
    return rx.box(
        bar_vendor(),
        width='100%',
        align='center'
    )