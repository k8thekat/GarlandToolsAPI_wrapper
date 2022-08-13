"""
Tests for wrapper for GarlandTools Search Endpoint
"""

from . import search


def test_search_is_ok():
    """
    Tests if an search request succeeds
    """
    response = search("Radiant")
    assert response.ok


def test_search_is_json():
    """
    Tests if an search request returns JSON
    """
    response = search("Radiant")
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, list)
