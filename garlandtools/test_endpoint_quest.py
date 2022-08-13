"""
Tests for wrapper for GarlandTools Quest Endpoint
"""

from . import quest, quests


def test_quest_is_ok():
    """
    Tests if an quest request succeeds
    """
    response = quest(65537)
    assert response.ok


def test_quest_is_json():
    """
    Tests if an quest request returns JSON
    """
    response = quest(65537)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_quests_is_ok():
    """
    Tests if an quests request succeeds
    """
    response = quests()
    assert response.ok


def test_quests_is_json():
    """
    Tests if an quests request returns JSON
    """
    response = quests()
    assert response.ok
    print(response.url)

    response_json = response.json()
    assert isinstance(response_json, dict)
