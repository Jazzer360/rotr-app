from typing import Callable

import reflex as rx

from rotr_app.components.navbar import NavState
from rotr_app.data.json_loader import load_activities_data
from rotr_app.template import template
from rotr_app.util import apply_start_end

# Load activities data from JSON
_activities_data = load_activities_data()
friday = _activities_data['friday']
saturday = _activities_data['saturday']

apply_start_end(friday)
apply_start_end(saturday)


def timing_component(
    func: Callable[[dict], tuple[rx.Component, rx.Component]]
) -> Callable[[dict], rx.Component]:
    def wrapper(activity: dict):
        return rx.cond(
            (activity['end'] > NavState.now) & (
                activity['start'] < NavState.now),
            func(activity)[0],
            rx.cond(
                (
                    (activity['start'] > NavState.now) &
                    (activity['start'] == activity['end']) &
                    (activity['start'] - NavState.now < 3600)
                ),
                func(activity)[1],
                rx.fragment()
            )
        )
    return wrapper


@timing_component
def badge(activity: dict) -> tuple[rx.Component, rx.Component]:
    return (
        rx.badge('In Progress', align_self='flex-end'),
        rx.badge('Starting Soon', align_self='flex-end', color_scheme='grass')
    )


@timing_component
def time_left_text(activity: dict) -> tuple[rx.Component, rx.Component]:
    return (
        rx.text(
            (activity['end'] - NavState.now) // 60,
            ' minutes left',
            align='right',
            flex_grow='1'
        ),
        rx.text(
            'Starts in ',
            (activity['start'] - NavState.now) // 60,
            ' minutes',
            align='right',
            flex_grow='1'
        )
    )


@timing_component
def progress_bar(activity: dict) -> tuple[rx.Component, rx.Component]:
    return (
        rx.progress(
            value=((NavState.now - activity['start']) /
                   (activity['end'] - activity['start']) * 100),
            margin_top='8px'
        ),
        rx.fragment()
    )


def activity_card(activity: dict) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.vstack(
                rx.hstack(
                    rx.text(activity['name'], font_weight='bold'),
                    rx.spacer(),
                    badge(activity),
                    width='100%'
                ),
                rx.hstack(
                    rx.icon('map-pin', size=16),
                    rx.text(activity['location']),
                    align='center'
                ),
                rx.hstack(
                    rx.text(activity['time']),
                    time_left_text(activity),
                    width='100%'
                ),
                width='100%'
            ),
            align='center',
            justify='start'
        ),
        progress_bar(activity),
        color=rx.cond(activity['end'] < NavState.now, 'gray', '')
    )


def activity_entry(activity: dict) -> rx.Component:
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
def activities_page() -> rx.Component:
    return rx.vstack(
        rx.heading('Friday'),
        rx.box(
            [activity_entry(activity) for activity in friday],
            width='100%'
        ),
        rx.heading('Saturday'),
        rx.box(
            [activity_entry(activity) for activity in saturday],
            width='100%'
        ),
        width='100%',
        align='center'
    )
