import reflex as rx
from typing import Callable

from rotr_app.components.navbar import NavState
from rotr_app.components.surveypopup import SurveyState
from rotr_app.data.json_loader import load_schedule_data
from rotr_app.template import template
from rotr_app.util.utils import apply_start_end

# Load schedule data from JSON
_schedule_data = load_schedule_data()
friday = _schedule_data['friday']
saturday = _schedule_data['saturday']

apply_start_end(friday)
apply_start_end(saturday)


class ScheduleState(rx.State):
    @rx.event
    def show_toast(self):
        yield NavState.update
        yield SurveyState.check_survey_status
        return rx.toast.info(
            'Click a band to learn more about them.',
            duration=5000,
            close_button=True
        )


def on_stage_component(
    component_function: Callable[[dict], rx.Component]
) -> Callable[[dict], rx.Component]:
    def wrapper(band: dict) -> rx.Component:
        return rx.cond(
            (band['start'] < NavState.now) & (band['end'] > NavState.now),
            component_function(band),
            rx.fragment()
        )
    return wrapper


@on_stage_component
def time_left_text(band: dict) -> rx.Component:
    return rx.text(
            (band['end'] - NavState.now) // 60,
            ' minutes left',
            align='right',
            flex_grow='1'
    )


@on_stage_component
def badge(band: dict) -> rx.Component:
    return rx.badge('On Stage', align_self='flex-end')


@on_stage_component
def progress(band: dict) -> rx.Component:
    return rx.progress(
        value=((NavState.now - band['start']) /
               (band['end'] - band['start']) * 100),
        margin_top='8px'
    )


def band_card(band: dict) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.text(
                band['stage'],
                size='1',
                writing_mode='vertical-lr',
                transform='scale(-1)'
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        band['name'],
                        font_weight=rx.cond(
                            band['stage'] == 'Main', 'bold', 'normal'
                        )
                    ),
                    rx.spacer(),
                    badge(band),
                    width='100%'
                ),
                rx.hstack(
                    rx.text(band['time']),
                    time_left_text(band),
                    width='100%'
                ),
                width='100%'
            ),
            align='center',
            justify='start'
        ),
        progress(band),
        color=rx.cond(band['end'] < NavState.now, 'gray', ''),
        margin_left=rx.cond(band['stage'] == 'Main', '0px', '20px')
    )


def link(band: dict, attr: str, icontag: str, text: str) -> rx.Component:
    return rx.cond(
        band.get(attr),
        rx.link(
            rx.hstack(
                rx.icon(tag=icontag),
                rx.text(text)
            ),
            href=band.get(attr)
        )
    )


def links(band: dict) -> rx.Component:
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


def band_entry(band: dict) -> rx.Component:
    return rx.container(
        rx.dialog.root(
            rx.dialog.trigger(
                band_card(band)
            ),
            rx.dialog.content(
                rx.hstack(
                    rx.dialog.title(band['name'], padding_top='8px'),
                    rx.spacer(),
                    rx.dialog.close(rx.icon('x'))
                ),
                rx.cond(band.get('img'), rx.image(src=band.get('img'))),
                rx.dialog.description(band.get('bio'), margin='12px 0px'),
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
            [band_entry(band) for band in friday],
            width='100%'
        ),
        rx.heading('Saturday'),
        rx.box(
            [band_entry(band) for band in saturday],
            width='100%'
        ),
        width='100%',
        align='center'
    )
