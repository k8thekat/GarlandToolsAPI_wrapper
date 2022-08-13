"""
Wrapper for GarlandTools Mob Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE, SESSION

GARLAND_TOOLS_MOB_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'mob/{GARLAND_TOOLS_LANGUAGE}/2/'
GARLAND_TOOLS_MOBS_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'browse/{GARLAND_TOOLS_LANGUAGE}/2/mob.json'


def mob(mob_id: int):
    """
    Returns an mob by id
    """
    result = SESSION.get(
        f'{GARLAND_TOOLS_MOB_ENDPOINT}{mob_id}.json')
    return result


def mobs():
    """
    Returns all mobs
    """
    result = SESSION.get(GARLAND_TOOLS_MOBS_ENDPOINT)
    return result
