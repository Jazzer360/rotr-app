from datetime import datetime
from typing import Type, TypeVar

import pytz

import reflex as rx

from ..components.navbar import NavState
from ..template import template
from ..util.utils import production, get_start_end

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
        if production():
            fri = '2024-07-12'
            sat = '2024-07-13'
        else:
            fri = datetime.now(
                pytz.timezone('America/Chicago')).strftime('%Y-%m-%d')
            sat = fri
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
            name='Face Painting',
            day='F',
            time='5:30pm - 7:00pm',
            loc="Children's Tent"),
        ActivityInfo.create(
            name='Rock Painting',
            day='F',
            time='5:30pm - 7:00pm',
            loc="Children's Tent"),
        ActivityInfo.create(
            name='History Tour with Mark Titus',
            day='F',
            time='6:30pm',
            loc='Museum'),
    ]
    saturday: list[ActivityInfo] = [
        ActivityInfo.create(
            name='Yoga',
            day='S',
            time='9:00am - 10:00am',
            loc='Main Stage'),
        ActivityInfo.create(
            name='Spoon Workshop',
            day='S',
            time='12:00pm - 2:00pm',
            loc='Information Booth'),
        ActivityInfo.create(
            name='Face Painting',
            day='S',
            time='1:30pm - 3:30pm',
            loc="Children's Tent"),
        ActivityInfo.create(
            name='Prairie Ecology Bus Center',
            day='S',
            time='2:30pm - 3:30pm',
            loc="Children's Tent"),
        ActivityInfo.create(
            name='History Tour with Mark Titus',
            day='S',
            time='2:30pm',
            loc='Museum'),
        ActivityInfo.create(
            name='Flower Crowns',
            day='S',
            time='3:30pm - 4:30pm',
            loc="Children's Tent"),
        ActivityInfo.create(
            name='Prairie Ecology Bus Center',
            day='S',
            time='4:30pm - 5:30pm',
            loc="Children's Tent"),
        ActivityInfo.create(
            name='Costume Parade',
            day='S',
            time='6:00pm - 6:30pm',
            loc="Children's Tent")
    ]    


def badge(activity: ActivityInfo) -> rx.Component:
    return rx.cond(  # Check if ended
        activity.end < NavState.now,
        rx.fragment(),
        rx.cond(  # Check if started
            activity.start < NavState.now,
            rx.badge('In Progress', align_self='flex-end'),
            rx.cond(  # Check if scheduled start
                activity.start == activity.end,
                rx.cond(
                    activity.start - NavState.now < 3600,
                    rx.badge(
                        'Starting Soon',
                        align_self='flex-end',
                        color_scheme='grass'),
                    rx.fragment()
                ),
                rx.fragment()
            )
        )
    )


def time_left_text(activity: ActivityInfo) -> rx.Component:
    return rx.cond(  # Check if ended
        activity.end < NavState.now,
        rx.fragment(),
        rx.cond(  # Check if started
            activity.start < NavState.now,
            rx.text(
                (activity.end - NavState.now) // 60,
                ' minutes left',
                align='right',
                flex_grow='1'
            ),
            rx.cond(  # Check if scheduled start
                activity.start == activity.end,
                rx.cond(
                    activity.start - NavState.now < 3600,
                    rx.text(
                        'Starts in ',
                        (activity.start - NavState.now) // 60,
                        ' minutes',
                        align='right',
                        flex_grow='1'
                    ),
                    rx.fragment()
                ),
                rx.fragment()
            )
        )
    )


def progress_bar(activity: ActivityInfo) -> rx.Component:
    return rx.cond(
        activity.start < NavState.now,
        rx.cond(
            activity.end > NavState.now,
            rx.progress(
                value=((NavState.now - activity.start) / 
                       (activity.end - activity.start) * 100),
                margin_top='8px'
            ),
            rx.fragment()
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
