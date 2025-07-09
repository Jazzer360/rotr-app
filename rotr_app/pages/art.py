import reflex as rx

from rotr_app.components.navbar import NavState
from rotr_app.data.json_loader import load_art_data
from rotr_app.template import template

# Load art data from JSON
_art_data = load_art_data()
vendors = _art_data['vendors']


def vendor_item(vendor: dict) -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.card(
                rx.heading(vendor.get('vendor'), margin_bottom='1em'),
                rx.text(
                    vendor.get('description'),
                    size='3',
                    font_style='italic'
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
    route='/art',
    title='Art Vendors',
    on_load=NavState.update)
@template
def art_page() -> rx.Component:
    return rx.box(
        [vendor_item(vendor) for vendor in vendors],
        width='100%',
        align='center'
    )
