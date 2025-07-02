import json
import os
from functools import lru_cache
from typing import Any, Dict, List


def get_data_path(filename: str) -> str:
    return os.path.join(os.path.dirname(__file__), 'static', filename)


@lru_cache(maxsize=None)
def load_json_data(filename: str) -> Dict[str, Any]:
    file_path = get_data_path(filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_schedule_data() -> Dict[str, List[Dict[str, Any]]]:
    return load_json_data('schedule.json')


def load_activities_data() -> Dict[str, List[Dict[str, Any]]]:
    return load_json_data('activities.json')


def load_food_data() -> Dict[str, List[Dict[str, Any]]]:
    return load_json_data('food.json')


def load_navbar_data() -> Dict[str, Dict[str, str]]:
    return load_json_data('navbar.json')
