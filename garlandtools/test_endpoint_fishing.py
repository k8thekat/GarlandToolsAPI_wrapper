"""
Tests for wrapper for GarlandTools Fishing Endpoint
"""

from . import fishing


def test_fishing_is_ok():
    """
    Tests if an fishing request succeeds
    """
    response = fishing()
    assert response.ok


def test_fishing_is_json():
    """
    Tests if an fishing request returns JSON
    """
    response = fishing()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)
