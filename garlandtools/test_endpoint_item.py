"""
Tests for wrapper for GarlandTools Item Endpoint
"""

from . import item


def test_item_is_ok():
    """
    Tests if an item request succeeds
    """
    response = item(2)
    assert response.ok

def test_item_is_json():
    """
    Tests if an item request returns JSON
    """
    response = item(2)
    response_json = response.json()
    assert type(response_json) is dict
