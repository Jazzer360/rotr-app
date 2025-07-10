import os
from datetime import datetime
from typing import Callable, Optional

import reflex as rx

from rotr_app.data import get_manager
from rotr_app.data.json_loader import load_navbar_data
from rotr_app.util.utils import festival_started

# Load navigation links from JSON
_navbar_data = load_navbar_data()
links = _navbar_data['links']

FRONTEND_VERSION = os.environ.get('COMMIT_SHA', '')


class Announcement(rx.Base):
    time: int
    user: str
    subject: str
    message: list[str]


class NavState(rx.State):
    now: int = 0
    last_post: int = 0
    last_update: int = 0
    last_post_read: str = rx.Cookie(
        't0',
        name='last_post',
        max_age=60 * 60 * 24 * 30
    )
    announcements: list[Announcement] = []
    current_version: str = rx.SessionStorage(name='current_version')

    @rx.var
    def show_survey(self) -> bool:
        _ = self.now
        return festival_started()

    @rx.var
    def show_volunteer(self) -> bool:
        _ = self.now
        return not festival_started()

    @rx.event
    def update(self, _=None):
        self.now = int(datetime.now().timestamp())
        if (self.last_update != get_manager().last_update):
            print('Found new announcements')
            self.last_update = get_manager().last_update
            self.last_post = get_manager().last_post
            posts = [Announcement(
                time=k,
                user=v.get('user') or '',
                subject=v.get('subject') or '',
                message=get_messages(v))
                for k, v in get_manager().posts.items()]
            posts.sort(key=lambda x: x.time, reverse=True)
            self.announcements = posts
            if int(self.last_post_read[1:]) < self.last_post:
                return NavState.show_announcement_toast

    @rx.event
    def set_read(self):
        self.last_post_read = 't' + str(self.last_post)

    @rx.event
    def show_announcement_toast(self):
        return rx.toast.warning('New announcements posted.')

    @rx.event
    def set_frontend_version(self):
        self.current_version = FRONTEND_VERSION

    @rx.event
    def check_version(self):
        if FRONTEND_VERSION != self.current_version:
            return rx.call_script('window.location.reload()')


def get_messages(post_data: dict[str, str]) -> list[str]:
    msg = post_data.get('message')
    messages = [m for m in msg.strip().split('\n') if m] if msg else ['']
    messages[0] = f'"{messages[0]}'
    messages[-1] = f'{messages[-1]}"'
    return messages


def get_survey_handler(link: str) -> Optional[Callable]:
    if link == 'Survey':
        from rotr_app.components.surveypopup import SurveyState
        return SurveyState.mark_survey_clicked
    return None


def navbar_link(link: tuple[str, str]) -> rx.Component:
    click_handler = get_survey_handler(link[0])
    return rx.link(
        rx.text(link[0], size='4', weight='medium'),
        href=link[1],
        is_external=not link[1].startswith('/'),
        on_click=click_handler,
        display=rx.cond(
            hide_link(link),
            'none',
            'block'
        )
    )


def hide_link(link):
    return ((~NavState.show_survey & (link[0] == 'Survey')) |
            (~NavState.show_volunteer & (link[0] == 'Volunteer')))


def menu_item(link: tuple[str, str]) -> rx.Component:
    click_handler = get_survey_handler(link[0])
    return rx.menu.item(
        rx.text(link[0], size='4', weight='medium'),
        on_select=rx.redirect(
            link[1],
            is_external=not link[1].startswith('/')
        ),
        color=rx.cond(
            (link[0] == 'Announcements') & unread_posts(),
            'red',
            ''
        ),
        on_click=click_handler,
        display=rx.cond(
            hide_link(link),
            'none',
            'flex'
        )
    )


def unread_posts() -> bool:
    return (NavState.last_post_read[1:].to(int)  # type: ignore
            < NavState.last_post)


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
        rx.moment(interval=5000, on_change=NavState.update, display='none'),
        rx.moment(
            interval=60000,
            on_change=NavState.check_version,
            display='none'
        ),
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading('Rhythm of the River', size='7', weight='bold'),
                    align_items='center',
                ),
                rx.hstack(
                    [navbar_link((label, ref))
                        for label, ref in links.items()],
                    rx.color_mode.button(),
                    justify='end',
                    spacing='5',
                    align_items='center',
                ),
                justify='between',
                align_items='center',
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading('Rhythm of the River', size='6', weight='bold'),
                    align_items='center',
                    flex_grow='1'
                ),
                rx.color_mode.button(),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.box(
                            rx.icon('menu', size=30),
                            rx.cond(unread_posts(), unread_badge())
                        )
                    ),
                    rx.menu.content(
                        [menu_item((label, ref))
                            for label, ref in links.items()]
                    ),
                    justify='end',
                ),
                justify='between',
                align_items='center',
            ),
        ),
        bg=rx.color('accent', 3),
        padding='1em',
        width='100%',
        on_mount=NavState.set_frontend_version,
    )
