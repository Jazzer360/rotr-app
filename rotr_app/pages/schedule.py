from datetime import datetime
from typing import Type, TypeVar

import pytz

import reflex as rx

from ..components.navbar import NavState
from ..template import template
from ..util.utils import production, get_start_end

T = TypeVar('T', bound='BandInfo')


class BandInfo(rx.Base):
    name: str
    time: str
    stage: str
    start: int
    end: int
    img: str = None
    bio: str = None
    web: str = None
    fb: str = None
    insta: str = None
    spotify: str = None
    apple: str = None
    yt: str = None

    @classmethod
    def create(cls: Type[T], *, name: str, day: str, time: str, stage: str,
               **kwargs: dict[str, str]) -> T:
        if production():
            fri = '2025-07-11'
            sat = '2025-07-12'
        else:
            fri = datetime.now(
                pytz.timezone('America/Chicago')).strftime('%Y-%m-%d')
            sat = fri
        date = fri if day == 'F' else sat
        return BandInfo(
            name=name,
            time=time,
            stage=stage,
            **(kwargs | get_start_end(date, time))
        )


class ScheduleState(rx.State):
    friday: list[BandInfo] = [
        BandInfo.create(
            name='',
            day='F',
            time='5:00pm - 6:00pm',
            stage='Main',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='F',
            time='6:00pm - 6:30pm',
            stage='Church',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='F',
            time='6:30pm - 7:30pm',
            stage='Main',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='F',
            time='7:30pm - 8:00pm',
            stage='Church',
            bio="""
                """,
            img='',
            fb='',
            insta='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='F',
            time='8:00pm - 9:00pm',
            stage='Main',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='F',
            time='9:00pm - 9:30pm',
            stage='Church',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='F',
            time='9:30pm - 11:00pm',
            stage='Main',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt='')
    ]
    saturday: list[BandInfo] = [
        BandInfo.create(
            name='',
            day='S',
            time='12:30pm - 1:30pm',
            stage='Main',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='S',
            time='1:30pm - 2:00pm',
            stage='Church',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='S',
            time='2:00pm - 3:00pm',
            stage='Main',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='S',
            time='3:00pm - 3:30pm',
            stage='Church',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='S',
            time='3:30pm - 4:30pm',
            stage='Main',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='S',
            time='4:30pm - 5:00pm',
            stage='Church',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='S',
            time='5:00pm - 6:00pm',
            stage='Main',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='S',
            time='6:00pm - 6:30pm',
            stage='Church',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='S',
            time='6:30pm - 7:30pm',
            stage='Main',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='S',
            time='7:30pm - 8:00pm',
            stage='Church',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='S',
            time='8:00pm - 9:00pm',
            stage='Main',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='S',
            time='9:00pm - 9:30pm',
            stage='Church',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt=''),
        BandInfo.create(
            name='',
            day='S',
            time='9:30pm - 11:00pm',
            stage='Main',
            bio="""
                """,
            img='',
            web='',
            fb='',
            insta='',
            spotify='',
            apple='',
            yt='')
    ]

    def show_toast(self):
        yield NavState.update
        return rx.toast.info(
            'Click a band to learn more about them.',
            duration=5000,
            close_button=True
        )


def on_stage_component(component_function):
    def wrapper(band: BandInfo):
        return rx.cond(
            (band.start < NavState.now) & (band.end > NavState.now),
            component_function(band),
            rx.fragment()
        )
    return wrapper


@on_stage_component
def time_left_text(band: BandInfo) -> rx.Component:
    return rx.text(
            (band.end - NavState.now) // 60,
            ' minutes left',
            align='right',
            flex_grow='1'
    )


@on_stage_component
def badge(band: BandInfo) -> rx.Component:
    return rx.badge('On Stage', align_self='flex-end')


@on_stage_component
def progress(band: BandInfo) -> rx.Component:
    return rx.progress(
        value=((NavState.now - band.start) / (band.end - band.start) * 100),
        margin_top='8px'
    )


def band_card(band: BandInfo) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.text(
                band.stage,
                size='1',
                writing_mode='vertical-lr',
                transform='scale(-1)'
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(band.name),
                    rx.spacer(),
                    badge(band),
                    width='100%'
                ),
                rx.hstack(
                    rx.text(band.time),
                    time_left_text(band),
                    width='100%'
                ),
                width='100%'
            ),
            align='center',
            justify='start'
        ),
        progress(band),
        color=rx.cond(band.end < NavState.now, 'gray', '')
    )


def link(band: BandInfo, attr: str, icontag: str, text: str) -> rx.Component:
    return rx.cond(
        getattr(band, attr, None),
        rx.link(
            rx.hstack(
                rx.icon(tag=icontag),
                rx.text(text)
            ),
            href=getattr(band, attr)
        )
    )


def links(band: BandInfo) -> rx.Component:
    return rx.flex(
        link(band, 'web', 'globe', 'Website'),
        link(band, 'fb', 'facebook', 'Facebook'),
        link(band, 'insta', 'instagram', 'Instagram'),
        link(band, 'spotify', 'audio-lines', 'Spotify'),
        link(band, 'apple', 'apple', 'iTunes'),
        link(band, 'yt', 'youtube', 'YouTube'),
        wrap='wrap',
        spacing='4'
    )


def band_entry(band: BandInfo) -> rx.Component:
    return rx.container(
        rx.dialog.root(
            rx.dialog.trigger(
                band_card(band)
            ),
            rx.dialog.content(
                rx.hstack(
                    rx.dialog.title(band.name, padding_top='8px'),
                    rx.spacer(),
                    rx.dialog.close(rx.icon('x'))
                ),
                rx.cond(band.img, rx.image(src=band.img)),
                rx.dialog.description(band.bio, margin='12px 0px'),
                links(band),
                rx.dialog.close(
                    rx.button('Close', margin_top='24px')
                )
            )
        ),
        size='1',
        padding='8px'
    )


@rx.page(
    route='/',
    title='Live Schedule',
    on_load=ScheduleState.show_toast)
@template
def schedule() -> rx.Component:
    return rx.vstack(
        rx.heading('Friday'),
        rx.box(
            rx.foreach(ScheduleState.friday, band_entry),
            width='100%'
        ),
        rx.heading('Saturday'),
        rx.box(
            rx.foreach(ScheduleState.saturday, band_entry),
            width='100%'
        ),
        width='100%',
        align='center'
    )
