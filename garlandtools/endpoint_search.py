"""
Wrapper for GarlandTools Search Endpoint
"""

from .globals import GARLAND_TOOLS_ENDPOINT, GARLAND_TOOLS_LANGUAGE, SESSION

GARLAND_TOOLS_SEARCH_ENDPOINT = f'{GARLAND_TOOLS_ENDPOINT}api/search.php'


def search(query: str):
    """
    Submits a search query and returns the results
    """
    result = SESSION.get(f'{GARLAND_TOOLS_SEARCH_ENDPOINT}'
                         + f'?text={query}&lang={GARLAND_TOOLS_LANGUAGE}')
    return result
