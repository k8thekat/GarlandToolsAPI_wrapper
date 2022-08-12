"""
Wrapper for GarlandTools Leve Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE, SESSION

GARLAND_TOOLS_LEVE_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'leve/{GARLAND_TOOLS_LANGUAGE}/3/'
GARLAND_TOOLS_LEVES_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'browse/{GARLAND_TOOLS_LANGUAGE}/2/leve.json'


def leve(leve_id: int):
    """
    Returns an leve by id
    """
    result = SESSION.get(
        f'{GARLAND_TOOLS_LEVE_ENDPOINT}{leve_id}.json')
    return result


def leves():
    """
    Returns all leves
    """
    result = SESSION.get(GARLAND_TOOLS_LEVES_ENDPOINT)
    return result
