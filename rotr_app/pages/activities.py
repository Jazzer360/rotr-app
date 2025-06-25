import reflex as rx

from ..components.navbar import NavState
from ..template import template
from ..util.utils import apply_start_end

friday = [
    {
        'name': 'Delafield Documentary Film',
        'day': 'F',
        'time': '6:00pm - 6:30pm',
        'location': 'Church'
    }
]

saturday = [
    {
        'name': 'Delafield Documentary Film',
        'day': 'S',
        'time': '12:30pm - 1:00pm',
        'location': 'Church'
    },
    {
        'name': 'Didgeridoo Workshop',
        'day': 'S',
        'time': '4:00pm - 4:30pm',
        'location': 'Church'
    },
    {
        'name': 'Delafield Documentary Film',
        'day': 'S',
        'time': '5:30pm - 6:00pm',
        'location': 'Church'
    },
]    

apply_start_end(friday)
apply_start_end(saturday)


def timing_component(component_function):
    def wrapper(activity: dict):
        return rx.cond(
            (activity['end'] > NavState.now) & (
                activity['start'] < NavState.now),
            component_function(activity)[0],
            rx.cond(
                (
                    (activity['start'] > NavState.now) &
                    (activity['start'] == activity['end']) &
                    (activity['start'] - NavState.now < 3600)
                ),
                component_function(activity)[1],
                rx.fragment()
            )
        )
    return wrapper


@timing_component
def badge(activity: dict) -> rx.Component:
    return (
        rx.badge('In Progress', align_self='flex-end'),
        rx.badge('Starting Soon', align_self='flex-end', color_scheme='grass')
    )


@timing_component
def time_left_text(activity: dict) -> rx.Component:
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
def progress_bar(activity: dict) -> rx.Component:
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
                rx.text(activity['location']),
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
def schedule() -> rx.Component:
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
