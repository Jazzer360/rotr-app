from functools import cache
from datetime import datetime

import pytz

from reflex.config import get_config


@cache
def production():
    config = get_config()
    print(f'Running on: {config.api_url}')
    return not config.api_url.startswith('http://localhost')


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
