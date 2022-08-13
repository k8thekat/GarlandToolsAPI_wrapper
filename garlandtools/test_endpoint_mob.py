"""
Tests for wrapper for GarlandTools Mob Endpoint
"""

from . import mob, mobs


def test_mob_is_ok():
    """
    Tests if an mob request succeeds
    """
    response = mob(20000000002)
    assert response.ok


def test_mob_is_json():
    """
    Tests if an mob request returns JSON
    """
    response = mob(20000000002)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_mobs_is_ok():
    """
    Tests if an mobs request succeeds
    """
    response = mobs()
    assert response.ok


def test_mobs_is_json():
    """
    Tests if an mobs request returns JSON
    """
    response = mobs()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)
