"""
Wrapper for GarlandTools Node Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE, SESSION

GARLAND_TOOLS_NODE_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'node/{GARLAND_TOOLS_LANGUAGE}/2/'
GARLAND_TOOLS_NODES_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}db/doc/' \
    + f'browse/{GARLAND_TOOLS_LANGUAGE}/2/node.json'


def node(node_id: int):
    """
    Returns an node by id
    """
    result = SESSION.get(
        f'{GARLAND_TOOLS_NODE_ENDPOINT}{node_id}.json')
    return result


def nodes():
    """
    Returns all nodes
    """
    result = SESSION.get(GARLAND_TOOLS_NODES_ENDPOINT)
    return result
