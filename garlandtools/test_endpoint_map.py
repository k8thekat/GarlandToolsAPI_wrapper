"""
Tests for wrapper for GarlandTools Map Endpoint
"""

from . import map


def test_map_is_ok():
    """
    Tests if an map request succeeds
    """
    response = map('La Noscea/Lower La Noscea')
    print(response.url)
    assert response.ok
