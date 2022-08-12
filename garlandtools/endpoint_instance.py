"""
Wrapper for GarlandTools Instance Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE, SESSION

GARLAND_TOOLS_INSTANCE_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'instance/{GARLAND_TOOLS_LANGUAGE}/2/'
GARLAND_TOOLS_INSTANCES_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'browse/{GARLAND_TOOLS_LANGUAGE}/2/instance.json'


def instance(instance_id: int):
    """
    Returns an instance by instance_id
    """
    result = SESSION.get(
        f'{GARLAND_TOOLS_INSTANCE_ENDPOINT}{instance_id}.json')
    return result


def instances():
    """
    Returns all instances
    """
    result = SESSION.get(GARLAND_TOOLS_INSTANCES_ENDPOINT)
    return result
