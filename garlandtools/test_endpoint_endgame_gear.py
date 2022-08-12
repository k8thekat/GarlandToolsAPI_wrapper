"""
Tests for wrapper for GarlandTools EndGame Gear Endpoint
"""

from . import endgame_gear, Job


def test_endgame_gear_is_ok():
    """
    Tests if an Endgame Gear request succeeds
    """
    response = endgame_gear(Job.WHITE_MAGE)
    assert response.ok


def test_endgame_gear_is_json():
    """
    Tests if an endgame_gear request returns JSON
    """
    response = endgame_gear(Job.WHITE_MAGE)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_endgame_gear_all_jobs():
    """
    Tests if an endgame_gear request returns JSON for all jobs
    """
    for job in Job:
        response = endgame_gear(job)
        assert response.ok

        response_json = response.json()
        assert isinstance(response_json, dict)
