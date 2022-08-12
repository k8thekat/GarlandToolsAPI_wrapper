"""
Globals
"""

import requests_cache

GARLAND_TOOLS_ENDPOINT = 'https://www.garlandtools.org/'
GARLAND_TOOLS_LANGUAGE = 'en'

SESSION = requests_cache.CachedSession(
    'garlandtools_cache', backend='sqlite', expire_after=3600)
