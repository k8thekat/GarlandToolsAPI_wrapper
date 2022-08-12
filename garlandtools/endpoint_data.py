"""
Wrapper for GarlandTools Data Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE, SESSION

GARLAND_TOOLS_DATA_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'core/{GARLAND_TOOLS_LANGUAGE}/3/data.json'


def data():
    """
    Returns all core data
    """
    result = SESSION.get(GARLAND_TOOLS_DATA_ENDPOINT)
    return result
