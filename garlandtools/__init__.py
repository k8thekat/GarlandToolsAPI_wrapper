"""
GarlandTools Python Module
"""

import requests_cache

__version__ = "0.1.0"
__author__ = 'Lukas Weber'
__credits__ = 'GarlandTools'

GARLAND_TOOLS_ENDPOINT = 'https://www.garlandtools.org'


session = requests_cache.CachedSession('garlandtools_cache', backend='sqlite', expire_after=3600)
result = session.get(GARLAND_TOOLS_ENDPOINT)
