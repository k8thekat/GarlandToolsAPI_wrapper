"""
Wrapper for GarlandTools Fishing Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE, SESSION

GARLAND_TOOLS_FISHING_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'browse/{GARLAND_TOOLS_LANGUAGE}/2/fishing.json'


def fishing():
    """
    Returns all fishing data
    """
    result = SESSION.get(GARLAND_TOOLS_FISHING_ENDPOINT)
    return result
