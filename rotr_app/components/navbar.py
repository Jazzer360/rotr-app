import reflex as rx

from ..data.firestore import posts, updated, Announcement


class NavState(rx.State):
    links: dict[str, str] = {
        'Schedule': '/',
        'Activities': '/activities',
        'Announcements': '/announcements',
        'Merch': 'https://rhythm-of-the-river-merch.printify.me/products',
        'Survey': 'https://docs.google.com/forms/d/e/1FAIpQLSdzPeKeD19qWza9q-Q8SpsKwCL7SnfrsO0Gdxauv1vVi3Co6w/viewform?usp=sf_link',
    }
    last_post: int = 0
    announcements: list[Announcement] = posts

    def on_poll(self, date=None):
        if int(self.last_post) < updated[0]:
            self.announcements = posts
            self.last_post = updated[0]


def navbar_link(link: list) -> rx.Component:
    return rx.link(
        rx.text(link[0], size="4", weight="medium"), href=link[1]
    )


def menu_item(link: list) -> rx.Component:
    return rx.menu.item(link[0], on_select=rx.redirect(link[1]))


def navbar() -> rx.Component:
    return rx.box(
        rx.moment(
            interval=1000,
            on_change=NavState.on_poll,
            display='none',
        ),
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Rhythm of the River", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    rx.foreach(NavState.links, navbar_link),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Rhythm of the River", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.foreach(NavState.links, menu_item)
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )
