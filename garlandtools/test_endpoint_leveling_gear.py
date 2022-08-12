"""
Tests for wrapper for GarlandTools Leveling gear Endpoint
"""

from . import leveling_gear, Job


def test_leveling_gear_is_ok():
    """
    Tests if an leveling_gear request succeeds
    """
    response = leveling_gear(Job.WHITE_MAGE)
    assert response.ok


def test_leveling_gear_is_json():
    """
    Tests if an leveling_gear request returns JSON
    """
    response = leveling_gear(Job.WHITE_MAGE)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_leveling_gear_all_jobs():
    """
    Tests if an leveling_gear request returns JSON for all jobs
    """
    for job in Job:
        response = leveling_gear(job)
        assert response.ok

        response_json = response.json()
        assert isinstance(response_json, dict)
