"""
Tests for wrapper for GarlandTools Instance Endpoint
"""

from . import instance, instances


def test_instance_is_ok():
    """
    Tests if an instance request succeeds
    """
    response = instance(1)
    assert response.ok


def test_instance_is_json():
    """
    Tests if an instance request returns JSON
    """
    response = instance(1)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_instances_is_ok():
    """
    Tests if an instances request succeeds
    """
    response = instances()
    assert response.ok


def test_instances_is_json():
    """
    Tests if an instances request returns JSON
    """
    response = instances()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)
