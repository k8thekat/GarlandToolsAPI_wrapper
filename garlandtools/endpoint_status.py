"""
Wrapper for GarlandTools Status Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE, SESSION

GARLAND_TOOLS_STATUS_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'Status/{GARLAND_TOOLS_LANGUAGE}/2/'
GARLAND_TOOLS_STATUSES_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'browse/{GARLAND_TOOLS_LANGUAGE}/2/status.json'


def status(status_id: int):
    """
    Returns a status by id
    """
    result = SESSION.get(f'{GARLAND_TOOLS_STATUS_ENDPOINT}{status_id}.json')
    return result


def statuses():
    """
    Returns all statuses
    """
    result = SESSION.get(f'{GARLAND_TOOLS_STATUSES_ENDPOINT}')
    return result
