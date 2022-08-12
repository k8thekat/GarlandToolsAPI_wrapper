"""
Tests for wrapper for GarlandTools Data Endpoint
"""

from . import data


def test_data_is_ok():
    """
    Tests if an data request succeeds
    """
    response = data()
    assert response.ok


def test_data_is_json():
    """
    Tests if an data request returns JSON
    """
    response = data()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)
