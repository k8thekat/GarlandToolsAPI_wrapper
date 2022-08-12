"""
Wrapper for GarlandTools Endgame Gear Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE, SESSION
from .job import Job

GARLAND_TOOLS_DATA_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'equip/{GARLAND_TOOLS_LANGUAGE}/2/end-'


def endgame_gear(job: Job):
    """
    Returns recommended endgame gear per job
    Use the common three letter abbreviation of the job.
    E.g.: White Mage => WHM; Warrior => WAR; Ninja => NIN
    """
    result = SESSION.get(f'{GARLAND_TOOLS_DATA_ENDPOINT}{job}.json')
    return result
