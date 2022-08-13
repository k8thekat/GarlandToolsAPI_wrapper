"""
Wrapper for GarlandTools NPC Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE, SESSION

GARLAND_TOOLS_NPC_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'npc/{GARLAND_TOOLS_LANGUAGE}/2/'
GARLAND_TOOLS_NPCS_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'browse/{GARLAND_TOOLS_LANGUAGE}/2/npc.json'


def npc(npc_id: int):
    """
    Returns an npc by id
    """
    result = SESSION.get(
        f'{GARLAND_TOOLS_NPC_ENDPOINT}{npc_id}.json')
    return result


def npcs():
    """
    Returns all npcs
    """
    result = SESSION.get(GARLAND_TOOLS_NPCS_ENDPOINT)
    return result
