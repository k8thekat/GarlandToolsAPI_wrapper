"""
Tests for wrapper for GarlandTools Status Endpoint
"""

from . import status, statuses


def test_status_is_ok():
    """
    Tests if an status request succeeds
    """
    response = status(1)
    assert response.ok


def test_status_is_json():
    """
    Tests if an status request returns JSON
    """
    response = status(1)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_statuses_is_ok():
    """
    Tests if an statuses request succeeds
    """
    response = statuses()
    assert response.ok


def test_statuses_is_json():
    """
    Tests if an statuses request returns JSON
    """
    response = statuses()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)
