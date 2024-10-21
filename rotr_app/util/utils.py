import os
from functools import cache, wraps
from datetime import datetime

import pytz

from reflex.config import get_config


@cache
def production():
    return False  # Remove this line for finished site
    config = get_config()
    print(f'Running on: {config.api_url}')
    return not config.api_url.startswith('http://localhost')


@cache
def compiling():
    return bool(os.environ.get('ROTR_COMPILE_ONLY'))


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


def no_compile(default=None):
    def inner_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return default if compiling() else func(*args, **kwargs)
        return wrapper
    return inner_decorator
