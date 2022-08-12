"""
Wrapper for GarlandTools Item Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE, SESSION

GARLAND_TOOLS_ITEM_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/item/{GARLAND_TOOLS_LANGUAGE}/3/'


def item(item_id: int):
    """
    Returns a item by id

    Format: PNG
    """
    result = SESSION.get(f'{GARLAND_TOOLS_ITEM_ENDPOINT}{item_id}.json')
    return result
