import asyncio
from datetime import datetime

import reflex as rx

from ..data.firestore import get_manager


class Announcement(rx.Base):
    time: int
    user: str
    subject: str
    message: list[str]


class NavState(rx.State):
    now: int = None
    running: bool = False
    links: dict[str, str] = {
        'Schedule': '/',
        'Activities': '/activities',
        'Announcements': '/announcements',
        'Merch': 'https://rhythm-of-the-river-merch.printify.me/products',
        'Survey': 'https://docs.google.com/forms/d/e/1FAIpQLSdzPeKeD19qWza9q-Q8SpsKwCL7SnfrsO0Gdxauv1vVi3Co6w/viewform?usp=sf_link',
    }
    last_post: int = 0
    last_read: str = rx.Cookie('0', max_age=60 * 60 * 24 * 30)
    announcements: list[Announcement] = []

    @rx.background
    async def update(self):
        async with self:
            if self.running:
                return
            self.running = True
        while True:
            async with self:
                self.now = int(datetime.now().timestamp())
            if self.last_post != get_manager().last_post:
                async with self:
                    print('Found new announcements')
                    self.last_post = get_manager().last_post
                    posts = [Announcement(
                        time=k,
                        user=v.get('user') or '',
                        subject=v.get('subject') or '',
                        message=get_messages(v))
                        for k, v in get_manager().posts.items()]
                    posts.sort(key=lambda x: x.time, reverse=True)
                    self.announcements = posts
            await asyncio.sleep(5)

    def set_read(self):
        self.last_read = str(self.last_post)
        return NavState.update


def get_messages(post_data: dict[str, str]) -> list[str]:
    msg = post_data.get('message')
    messages = [m for m in msg.strip().split('\n') if m] if msg else ['']
    messages[0] = f'"{messages[0]}'
    messages[-1] = f'{messages[-1]}"'
    return messages


def navbar_link(link: list) -> rx.Component:
    return rx.link(
        rx.text(link[0], size="4", weight="medium"), href=link[1]
    )


def menu_item(link: list) -> rx.Component:
    return rx.menu.item(
        link[0],
        on_select=rx.redirect(link[1]),
        color=rx.cond(
            (link[0] == 'Announcements') & unread_posts(),
            'red',
            ''
        )
    )


def unread_posts():
    return NavState.last_read.to(int) < NavState.last_post


def unread_badge() -> rx.Component:
    return rx.icon(
        'megaphone',
        position='absolute',
        top='.75em',
        right='.65em',
        size=20,
        background='red',
        border_radius='10px',
        padding='2px'
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading("Rhythm of the River", size="7", weight="bold"),
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
                    rx.heading("Rhythm of the River", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.box(
                            rx.icon("menu", size=30),
                            rx.cond(unread_posts(), unread_badge())
                        )
                    ),
                    rx.menu.content(rx.foreach(NavState.links, menu_item)),
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
