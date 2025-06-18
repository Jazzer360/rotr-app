from typing import Optional

import reflex as rx

from ..components.navbar import NavState
from ..template import template


class MenuItem(rx.Base):
    item: str
    desc: Optional[str]


class VendorMenu(rx.Base):
    vendor: str
    item_list: list[MenuItem]


class FoodState(rx.State):
    menus: list[VendorMenu] = [
        VendorMenu(
            vendor='Brady\'s Famous Chicken Wings',
            item_list=[
                MenuItem(
                    item='Chicken Wings',
                    desc="""
                         Sauce Flavors: Traditional, BBQ, Teriyaki, Spicy
                         Garlic, and Hot Chipotle
                         """
                ),
                MenuItem(
                    item='Celery w/ Ranch or Blue Cheese',
                    desc="""
                         Fresh Celery with a side of either Ranch or Blue
                         Cheese dressing
                         """
                )
            ]
        ),
        VendorMenu(
            vendor='Brady\'s Famous Chicken Wings',
            item_list=[
                MenuItem(
                    item='Chicken Wings',
                    desc="""
                         Sauce Flavors: Traditional, BBQ, Teriyaki, Spicy
                         Garlic, and Hot Chipotle
                         """
                ),
                MenuItem(
                    item='Celery w/ Ranch or Blue Cheese',
                    # desc="""
                    #      Fresh Celery with a side of either Ranch or Blue
                    #      Cheese dressing
                    #      """
                )
            ]
        )
    ]


def menu_item(item: MenuItem) -> rx.Component:
    return rx.vstack(
        rx.text(item.item, size='3'),
        rx.text(item.desc, size='2', margin_left='2em', font_style='italic')
    )


def vendor_item(menu: VendorMenu) -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading(menu.vendor),
            rx.card(
                rx.vstack(
                    rx.foreach(menu.item_list, menu_item)
                )
            )
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
        rx.foreach(FoodState.menus, vendor_item),
        width='100%',
        align='center'
    )
