"""
Tests for GarlandTools Class
"""

from . import GarlandTools, Job


def make_test_garlandtools():
    return GarlandTools()

# -----------------------------------------------------------------------------


def test_achievement_is_ok():
    """
    Tests if an achievement request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.achievement(1)
    assert response.ok


def test_achievement_is_json():
    """
    Tests if an achievement request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.achievement(1)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_achievements_is_ok():
    """
    Tests if an achievements request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.achievements()
    assert response.ok


def test_achievements_is_json():
    """
    Tests if an achievements request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.achievements()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_data_is_ok():
    """
    Tests if an data request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.data()
    assert response.ok


def test_data_is_json():
    """
    Tests if an data request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.data()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_endgame_gear_is_ok():
    """
    Tests if an Endgame Gear request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.endgame_gear(Job.WHITE_MAGE)
    assert response.ok


def test_endgame_gear_is_json():
    """
    Tests if an endgame_gear request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.endgame_gear(Job.WHITE_MAGE)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_endgame_gear_all_jobs():
    """
    Tests if an endgame_gear request returns JSON for all jobs
    """
    for job in Job:
        garlandtools = make_test_garlandtools()
        response = garlandtools.endgame_gear(job)
        assert response.ok

        response_json = response.json()
        assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_fate_is_ok():
    """
    Tests if an fate request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.fate(
        1631)   # Don't even ask me why it's starting at that number.
    # This is one of the first Lv1 FATEs.
    assert response.ok


def test_fate_is_json():
    """
    Tests if an fate request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.fate(
        1631)   # Don't even ask me why it's starting at that number.
    # This is one of the first Lv1 FATEs.
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_fates_is_ok():
    """
    Tests if an fates request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.fates()
    assert response.ok


def test_fates_is_json():
    """
    Tests if an fates request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.fates()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_fishing_is_ok():
    """
    Tests if an fishing request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.fishing()
    assert response.ok


def test_fishing_is_json():
    """
    Tests if an fishing request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.fishing()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_icon_is_ok():
    """
    Tests if an icon request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.icon('item', 22614)
    assert response.ok

# -----------------------------------------------------------------------------


def test_instance_is_ok():
    """
    Tests if an instance request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.instance(1)
    assert response.ok


def test_instance_is_json():
    """
    Tests if an instance request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.instance(1)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_instances_is_ok():
    """
    Tests if an instances request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.instances()
    assert response.ok


def test_instances_is_json():
    """
    Tests if an instances request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.instances()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_item_is_ok():
    """
    Tests if an item request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.item(2)
    assert response.ok


def test_item_is_json():
    """
    Tests if an item request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.item(2)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_leve_is_ok():
    """
    Tests if an leve request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.leve(21)
    assert response.ok


def test_leve_is_json():
    """
    Tests if an leve request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.leve(21)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_leves_is_ok():
    """
    Tests if an leves request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.leves()
    assert response.ok


def test_leves_is_json():
    """
    Tests if an leves request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.leves()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_leveling_gear_is_ok():
    """
    Tests if an leveling_gear request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.leveling_gear(Job.WHITE_MAGE)
    assert response.ok


def test_leveling_gear_is_json():
    """
    Tests if an leveling_gear request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.leveling_gear(Job.WHITE_MAGE)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_leveling_gear_all_jobs():
    """
    Tests if an leveling_gear request returns JSON for all jobs
    """
    for job in Job:
        garlandtools = make_test_garlandtools()
        response = garlandtools.leveling_gear(job)
        assert response.ok

        response_json = response.json()
        assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_map_zone_is_ok():
    """
    Tests if an map request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.map_zone('La Noscea/Lower La Noscea')
    assert response.ok

# -----------------------------------------------------------------------------


def test_mob_is_ok():
    """
    Tests if an mob request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.mob(20000000002)
    assert response.ok


def test_mob_is_json():
    """
    Tests if an mob request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.mob(20000000002)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_mobs_is_ok():
    """
    Tests if an mobs request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.mobs()
    assert response.ok


def test_mobs_is_json():
    """
    Tests if an mobs request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.mobs()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_node_is_ok():
    """
    Tests if an node request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.node(153)
    assert response.ok


def test_node_is_json():
    """
    Tests if an node request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.node(153)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_nodes_is_ok():
    """
    Tests if an nodes request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.nodes()
    assert response.ok


def test_nodes_is_json():
    """
    Tests if an nodes request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.nodes()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_npc_is_ok():
    """
    Tests if an npc request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.npc(1000063)
    assert response.ok


def test_npc_is_json():
    """
    Tests if an npc request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.npc(1000063)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_npcs_is_ok():
    """
    Tests if an npcs request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.npcs()
    assert response.ok


def test_npcs_is_json():
    """
    Tests if an npcs request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.npcs()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_quest_is_ok():
    """
    Tests if an quest request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.quest(65537)
    assert response.ok


def test_quest_is_json():
    """
    Tests if an quest request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.quest(65537)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_quests_is_ok():
    """
    Tests if an quests request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.quests()
    assert response.ok


def test_quests_is_json():
    """
    Tests if an quests request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.quests()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_search_is_ok():
    """
    Tests if an search request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.search("Radiant")
    assert response.ok


def test_search_is_json():
    """
    Tests if an search request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.search("Radiant")
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, list)

# -----------------------------------------------------------------------------


def test_status_is_ok():
    """
    Tests if an status request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.status(1)
    assert response.ok


def test_status_is_json():
    """
    Tests if an status request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.status(1)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_statuses_is_ok():
    """
    Tests if an statuses request succeeds
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.statuses()
    assert response.ok


def test_statuses_is_json():
    """
    Tests if an statuses request returns JSON
    """
    garlandtools = make_test_garlandtools()
    response = garlandtools.statuses()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)
