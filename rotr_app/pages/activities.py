from typing import Type, TypeVar

import reflex as rx

from ..components.navbar import NavState
from ..template import template
from ..util.utils import get_start_end

T = TypeVar('T', bound='ActivityInfo')


class ActivityInfo(rx.Base):
    name: str
    time: str
    start: int
    end: int
    location: str

    @classmethod
    def create(cls: Type[T], *, name: str, day: str, time: str, loc: str,
               **kwargs: dict[str, str]) -> T:
        fri = '2025-07-11'
        sat = '2025-07-12'
        date = fri if day == 'F' else sat
        return ActivityInfo(
            name=name,
            time=time,
            location=loc,
            **(kwargs | get_start_end(date, time))
        )


class ActivityState(rx.State):
    friday: list[ActivityInfo] = [
        ActivityInfo.create(
            name='Delafield Documentary Film',
            day='F',
            time='5:30pm - 6:00pm',
            loc='Church'),
    ]
    saturday: list[ActivityInfo] = [
        ActivityInfo.create(
            name='Didgeridoo Workshop',
            day='S',
            time='4:00pm - 4:30pm',
            loc='Church'),
        ActivityInfo.create(
            name='Delafield Documentary Film',
            day='S',
            time='5:30pm - 6:00pm',
            loc='Church'),
    ]    


def timing_component(component_function):
    def wrapper(activity: ActivityInfo):
        return rx.cond(
            (activity.end > NavState.now) & (activity.start < NavState.now),
            component_function(activity)[0],
            rx.cond(
                (
                    (activity.start > NavState.now) &
                    (activity.start == activity.end) &
                    (activity.start - NavState.now < 3600)
                ),
                component_function(activity)[1],
                rx.fragment()
            )
        )
    return wrapper


@timing_component
def badge(activity: ActivityInfo) -> rx.Component:
    return (
        rx.badge('In Progress', align_self='flex-end'),
        rx.badge('Starting Soon', align_self='flex-end', color_scheme='grass')
    )


@timing_component
def time_left_text(activity: ActivityInfo) -> rx.Component:
    return (
        rx.text(
            (activity.end - NavState.now) // 60,
            ' minutes left',
            align='right',
            flex_grow='1'
        ),
        rx.text(
            'Starts in ',
            (activity.start - NavState.now) // 60,
            ' minutes',
            align='right',
            flex_grow='1'
        )
    )


@timing_component
def progress_bar(activity: ActivityInfo) -> rx.Component:
    return (
        rx.progress(
            value=((NavState.now - activity.start) / 
                   (activity.end - activity.start) * 100),
            margin_top='8px'
        ),
        rx.fragment()
    )


def activity_card(activity: ActivityInfo) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.vstack(
                rx.hstack(
                    rx.text(activity.name),
                    rx.spacer(),
                    badge(activity),
                    width='100%'
                ),
                rx.text(activity.location),
                rx.hstack(
                    rx.text(activity.time),
                    time_left_text(activity),
                    width='100%'
                ),
                width='100%'
            ),
            align='center',
            justify='start'
        ),
        progress_bar(activity),
        color=rx.cond(activity.end < NavState.now, 'gray', '')
    )


def activity_entry(activity: ActivityInfo) -> rx.Component:
    return rx.container(
        activity_card(activity),
        size='1',
        padding='8px'
    )


@rx.page(
    route='/activities',
    title='Activity Schedule',
    on_load=NavState.update)
@template
def schedule() -> rx.Component:
    return rx.vstack(
        rx.heading('Friday'),
        rx.box(
            rx.foreach(ActivityState.friday, activity_entry),
            width='100%'
        ),
        rx.heading('Saturday'),
        rx.box(
            rx.foreach(ActivityState.saturday, activity_entry),
            width='100%'
        ),
        width='100%',
        align='center'
    )
