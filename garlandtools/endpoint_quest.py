"""
Wrapper for GarlandTools Quest Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE, SESSION

GARLAND_TOOLS_QUEST_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'quest/{GARLAND_TOOLS_LANGUAGE}/2/'
GARLAND_TOOLS_QUESTS_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'browse/{GARLAND_TOOLS_LANGUAGE}/2/quest.json'


def quest(quest_id: int):
    """
    Returns an quest by id
    """
    result = SESSION.get(
        f'{GARLAND_TOOLS_QUEST_ENDPOINT}{quest_id}.json')
    return result


def quests():
    """
    Returns all quests
    """
    result = SESSION.get(GARLAND_TOOLS_QUESTS_ENDPOINT)
    return result
