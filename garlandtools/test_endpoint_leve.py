"""
Tests for wrapper for GarlandTools Leve Endpoint
"""

from . import leve, leves


def test_leve_is_ok():
    """
    Tests if an leve request succeeds
    """
    response = leve(21)
    assert response.ok


def test_leve_is_json():
    """
    Tests if an leve request returns JSON
    """
    response = leve(21)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_leves_is_ok():
    """
    Tests if an leves request succeeds
    """
    response = leves()
    assert response.ok


def test_leves_is_json():
    """
    Tests if an leves request returns JSON
    """
    response = leves()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)
