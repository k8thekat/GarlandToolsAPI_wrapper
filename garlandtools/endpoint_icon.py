"""
Wrapper for GarlandTools Icon Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, SESSION

GARLAND_TOOLS_ICON_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}files/icons/'


def icon(icon_type: str, icon_id: int):
    """
    Returns a specific icon by icon_type and icon_id
    """
    result = SESSION.get(
        f'{GARLAND_TOOLS_ICON_ENDPOINT}{icon_type}/{icon_id}.png')
    return result
