"""
JSON data loader utility for loading static configuration data.
"""
import json
import os
from functools import lru_cache
from typing import Any, Dict, List


def get_data_path(filename: str) -> str:
    """Get the full path to a static data file."""
    return os.path.join(os.path.dirname(__file__), 'static', filename)


@lru_cache(maxsize=None)
def load_json_data(filename: str) -> Dict[str, Any]:
    """
    Load JSON data from a file in the static data directory.
    Results are cached for performance.
    
    Args:
        filename: The name of the JSON file to load
        
    Returns:
        The parsed JSON data as a dictionary
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    file_path = get_data_path(filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_schedule_data() -> Dict[str, List[Dict[str, Any]]]:
    """Load band schedule data for Friday and Saturday."""
    return load_json_data('schedule.json')


def load_activities_data() -> Dict[str, List[Dict[str, Any]]]:
    """Load activity schedule data for Friday and Saturday."""
    return load_json_data('activities.json')


def load_food_data() -> Dict[str, List[Dict[str, Any]]]:
    """Load food vendor data."""
    return load_json_data('food.json')


def load_navbar_data() -> Dict[str, Dict[str, str]]:
    """Load navigation links data."""
    return load_json_data('navbar.json')