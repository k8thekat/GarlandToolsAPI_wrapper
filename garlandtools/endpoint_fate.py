"""
Wrapper for GarlandTools Fate Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE, SESSION

GARLAND_TOOLS_FATE_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'fate/{GARLAND_TOOLS_LANGUAGE}/2/'
GARLAND_TOOLS_FATES_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'browse/{GARLAND_TOOLS_LANGUAGE}/2/fate.json'


def fate(fate_id: int):
    """
    Returns an fate by id
    """
    result = SESSION.get(
        f'{GARLAND_TOOLS_FATE_ENDPOINT}{fate_id}.json')
    return result


def fates():
    """
    Returns all fates
    """
    result = SESSION.get(GARLAND_TOOLS_FATES_ENDPOINT)
    return result
