"""
Wrapper for GarlandTools Item Endpoint
"""

from .globals import *

GARLAND_TOOLS_ITEM_ENDPOINT = "{}db/doc/item/{}/3/".format(GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE)


def item(item_id: int):
    """
    Returns a item by id
    """
    result = SESSION.get("{}{}.json".format(GARLAND_TOOLS_ITEM_ENDPOINT, item_id))
    return result
