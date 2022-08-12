"""
Wrapper for GarlandTools Map Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, SESSION

GARLAND_TOOLS_MAP_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}files/maps/'


def map_zone(zone: str):
    """
    Returns a specific map by the zone.
    Some zones require the parent zone as well.
    E.g.: La Noscea/Lower La Noscea

    Format: PNG
    """
    result = SESSION.get(
        f'{GARLAND_TOOLS_MAP_ENDPOINT}{zone}.png')
    return result
