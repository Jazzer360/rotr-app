import os
from functools import cache
from datetime import datetime, date

import pytz

from rotr_app.data.json_loader import load_schedule_data


@cache
def production() -> bool:
    env = os.getenv('REFLEX_ENV')
    if env and env.lower() == 'production':
        print('Running in production mode.')
        return True
    else:
        print('Running in development mode.')
        return False


@cache
def tz_offset(datestr) -> str:
    return pytz.timezone('America/Chicago').localize(
        datetime.fromisoformat(datestr + ' 12:00:00')).strftime('%z')


@cache
def get_datetime(date: str, time: str) -> datetime:
    return datetime.strptime(
        f'{date} {time} {tz_offset(date)}',
        '%Y-%m-%d %I:%M%p %z')


@cache
def get_start_end(date: str, time_range: str) -> dict[str, int]:
    pair = time_range.split(' - ')
    start = pair[0]
    end = pair[1] if len(pair) == 2 else pair[0]
    return {
        'start': int(get_datetime(date, start).timestamp()),
        'end': int(get_datetime(date, end).timestamp())
    }


@cache
def date_from_day(day) -> str:
    if production():
        return '2025-07-11' if day == 'F' else '2025-07-12'
    return date.today().isoformat()


def apply_start_end(data) -> None:
    for dataset in data:
        date = date_from_day(dataset['day'])
        dataset |= get_start_end(date, dataset['time'])


def festival_started() -> bool:
    first_band_time = load_schedule_data()['friday'][0]['time']
    first_band_time = first_band_time.split(' - ')[0]
    friday_date = date_from_day('F')
    first_band_dt = get_datetime(friday_date, first_band_time)
    now = datetime.now(first_band_dt.tzinfo)
    return now >= first_band_dt


def festival_over() -> bool:
    last_event_time = load_schedule_data()['saturday'][-1]['time']
    last_event_time = last_event_time.split(' - ')[-1]
    saturday_date = date_from_day('S')
    last_event_dt = get_datetime(saturday_date, last_event_time)
    now = datetime.now(last_event_dt.tzinfo)
    return now > last_event_dt
