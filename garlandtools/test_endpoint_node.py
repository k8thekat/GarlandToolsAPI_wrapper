"""
Tests for wrapper for GarlandTools Node Endpoint
"""

from . import node, nodes


def test_node_is_ok():
    """
    Tests if an node request succeeds
    """
    response = node(153)
    assert response.ok


def test_node_is_json():
    """
    Tests if an node request returns JSON
    """
    response = node(153)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_nodes_is_ok():
    """
    Tests if an nodes request succeeds
    """
    response = nodes()
    assert response.ok


def test_nodes_is_json():
    """
    Tests if an nodes request returns JSON
    """
    response = nodes()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)
