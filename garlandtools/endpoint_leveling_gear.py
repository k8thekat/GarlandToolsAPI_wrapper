"""
Wrapper for GarlandTools Leveling Gear Endpoint
"""

from .job import Job
from .globals import GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE, SESSION

GARLAND_TOOLS_LEVELLING_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'equip/{GARLAND_TOOLS_LANGUAGE}/2/leveling-'


def leveling_gear(job: Job):
    """
    Returns levelling gear based on job
    """
    result = SESSION.get(f'{GARLAND_TOOLS_LEVELLING_ENDPOINT}{job}.json')
    return result
