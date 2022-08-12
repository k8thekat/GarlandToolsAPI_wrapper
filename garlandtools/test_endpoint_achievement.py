"""
Tests for wrapper for GarlandTools Achievement Endpoint
"""

from . import achievement, achievements


def test_achievement_is_ok():
    """
    Tests if an achievement request succeeds
    """
    response = achievement(1)
    assert response.ok


def test_achievement_is_json():
    """
    Tests if an achievement request returns JSON
    """
    response = achievement(1)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_achievements_is_ok():
    """
    Tests if an achievements request succeeds
    """
    response = achievements()
    assert response.ok


def test_achievements_is_json():
    """
    Tests if an achievements request returns JSON
    """
    response = achievements()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)
