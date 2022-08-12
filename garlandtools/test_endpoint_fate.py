"""
Tests for wrapper for GarlandTools Fate Endpoint
"""

from . import fate, fates


def test_fate_is_ok():
    """
    Tests if an fate request succeeds
    """
    response = fate(
        1631)   # Don't even ask me why it's starting at that number.
    # This is one of the first Lv1 FATEs.
    assert response.ok


def test_fate_is_json():
    """
    Tests if an fate request returns JSON
    """
    response = fate(
        1631)   # Don't even ask me why it's starting at that number.
    # This is one of the first Lv1 FATEs.
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_fates_is_ok():
    """
    Tests if an fates request succeeds
    """
    response = fates()
    assert response.ok


def test_fates_is_json():
    """
    Tests if an fates request returns JSON
    """
    response = fates()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)
