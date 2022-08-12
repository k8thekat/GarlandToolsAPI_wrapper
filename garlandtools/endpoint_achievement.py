"""
Wrapper for GarlandTools Achievement Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE, SESSION

GARLAND_TOOLS_ACHIEVEMENT_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'achievement/{GARLAND_TOOLS_LANGUAGE}/2/'
GARLAND_TOOLS_ACHIEVEMENTS_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'browse/{GARLAND_TOOLS_LANGUAGE}/2/achievement.json'


def achievement(achievement_id: int):
    """
    Returns an achievement by id
    """
    result = SESSION.get(
        f'{GARLAND_TOOLS_ACHIEVEMENT_ENDPOINT}{achievement_id}.json')
    return result


def achievements():
    """
    Returns all achievements
    """
    result = SESSION.get(GARLAND_TOOLS_ACHIEVEMENTS_ENDPOINT)
    return result
