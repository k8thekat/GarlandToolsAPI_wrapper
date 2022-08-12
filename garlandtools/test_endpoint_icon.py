"""
Tests for wrapper for GarlandTools Icon Endpoint
"""

from . import icon


def test_icon_is_ok():
    """
    Tests if an icon request succeeds
    """
    response = icon('item', 22614)
    assert response.ok
