"""
Tests for wrapper for GarlandTools NPC Endpoint
"""

from . import npc, npcs


def test_npc_is_ok():
    """
    Tests if an npc request succeeds
    """
    response = npc(1000063)
    assert response.ok


def test_npc_is_json():
    """
    Tests if an npc request returns JSON
    """
    response = npc(1000063)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_npcs_is_ok():
    """
    Tests if an npcs request succeeds
    """
    response = npcs()
    assert response.ok


def test_npcs_is_json():
    """
    Tests if an npcs request returns JSON
    """
    response = npcs()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)
