"""
Tests for wrapper for GarlandTools Map Endpoint
"""

from . import map_zone


def test_map_zone_is_ok():
    """
    Tests if an map request succeeds
    """
    response = map_zone('La Noscea/Lower La Noscea')
    assert response.ok
