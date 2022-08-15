"""
Tests for GarlandTools Class
"""

from . import GarlandTools, Job


def test_garlandtools():
    """
    Tests if the GarlandTools class is instantiated correctly
    """
    cache_location = "cache/garlandtools_test_cache"
    cache_expire_after = 86400
    language = "en"

    api = GarlandTools(
        cache_location=cache_location, cache_expire_after=cache_expire_after, language=language)
    assert api.cache_location == cache_location
    assert api.cache_expire_after == cache_expire_after
    assert api.language == language

    return api

# -----------------------------------------------------------------------------


def test_achievement_is_ok():
    """
    Tests if an achievement request succeeds
    """
    api = test_garlandtools()
    response = api.achievement(1)
    assert response.ok


def test_achievement_is_json():
    """
    Tests if an achievement request returns JSON
    """
    api = test_garlandtools()
    response = api.achievement(1)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_achievements_is_ok():
    """
    Tests if an achievements request succeeds
    """
    api = test_garlandtools()
    response = api.achievements()
    assert response.ok


def test_achievements_is_json():
    """
    Tests if an achievements request returns JSON
    """
    api = test_garlandtools()
    response = api.achievements()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_data_is_ok():
    """
    Tests if an data request succeeds
    """
    api = test_garlandtools()
    response = api.data()
    assert response.ok


def test_data_is_json():
    """
    Tests if an data request returns JSON
    """
    api = test_garlandtools()
    response = api.data()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_endgame_gear_is_ok():
    """
    Tests if an Endgame Gear request succeeds
    """
    api = test_garlandtools()
    response = api.endgame_gear(Job.WHITE_MAGE)
    assert response.ok


def test_endgame_gear_is_json():
    """
    Tests if an endgame_gear request returns JSON
    """
    api = test_garlandtools()
    response = api.endgame_gear(Job.WHITE_MAGE)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_endgame_gear_all_jobs():
    """
    Tests if an endgame_gear request returns JSON for all jobs
    """
    for job in Job:
        api = test_garlandtools()
        response = api.endgame_gear(job)
        assert response.ok

        response_json = response.json()
        assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_fate_is_ok():
    """
    Tests if an fate request succeeds
    """
    api = test_garlandtools()
    response = api.fate(
        1631)   # Don't even ask me why it's starting at that number.
    # This is one of the first Lv1 FATEs.
    assert response.ok


def test_fate_is_json():
    """
    Tests if an fate request returns JSON
    """
    api = test_garlandtools()
    response = api.fate(
        1631)   # Don't even ask me why it's starting at that number.
    # This is one of the first Lv1 FATEs.
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_fates_is_ok():
    """
    Tests if an fates request succeeds
    """
    api = test_garlandtools()
    response = api.fates()
    assert response.ok


def test_fates_is_json():
    """
    Tests if an fates request returns JSON
    """
    api = test_garlandtools()
    response = api.fates()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_fishing_is_ok():
    """
    Tests if an fishing request succeeds
    """
    api = test_garlandtools()
    response = api.fishing()
    assert response.ok


def test_fishing_is_json():
    """
    Tests if an fishing request returns JSON
    """
    api = test_garlandtools()
    response = api.fishing()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_icon_is_ok():
    """
    Tests if an icon request succeeds
    """
    api = test_garlandtools()
    response = api.icon('item', 22614)
    assert response.ok

# -----------------------------------------------------------------------------


def test_instance_is_ok():
    """
    Tests if an instance request succeeds
    """
    api = test_garlandtools()
    response = api.instance(1)
    assert response.ok


def test_instance_is_json():
    """
    Tests if an instance request returns JSON
    """
    api = test_garlandtools()
    response = api.instance(1)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_instances_is_ok():
    """
    Tests if an instances request succeeds
    """
    api = test_garlandtools()
    response = api.instances()
    assert response.ok


def test_instances_is_json():
    """
    Tests if an instances request returns JSON
    """
    api = test_garlandtools()
    response = api.instances()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_item_is_ok():
    """
    Tests if an item request succeeds
    """
    api = test_garlandtools()
    response = api.item(2)
    assert response.ok


def test_item_is_json():
    """
    Tests if an item request returns JSON
    """
    api = test_garlandtools()
    response = api.item(2)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_leve_is_ok():
    """
    Tests if an leve request succeeds
    """
    api = test_garlandtools()
    response = api.leve(21)
    assert response.ok


def test_leve_is_json():
    """
    Tests if an leve request returns JSON
    """
    api = test_garlandtools()
    response = api.leve(21)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_leves_is_ok():
    """
    Tests if an leves request succeeds
    """
    api = test_garlandtools()
    response = api.leves()
    assert response.ok


def test_leves_is_json():
    """
    Tests if an leves request returns JSON
    """
    api = test_garlandtools()
    response = api.leves()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_leveling_gear_is_ok():
    """
    Tests if an leveling_gear request succeeds
    """
    api = test_garlandtools()
    response = api.leveling_gear(Job.WHITE_MAGE)
    assert response.ok


def test_leveling_gear_is_json():
    """
    Tests if an leveling_gear request returns JSON
    """
    api = test_garlandtools()
    response = api.leveling_gear(Job.WHITE_MAGE)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_leveling_gear_all_jobs():
    """
    Tests if an leveling_gear request returns JSON for all jobs
    """
    for job in Job:
        api = test_garlandtools()
        response = api.leveling_gear(job)
        assert response.ok

        response_json = response.json()
        assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_map_zone_is_ok():
    """
    Tests if an map request succeeds
    """
    api = test_garlandtools()
    response = api.map_zone('La Noscea/Lower La Noscea')
    assert response.ok

# -----------------------------------------------------------------------------


def test_mob_is_ok():
    """
    Tests if an mob request succeeds
    """
    api = test_garlandtools()
    response = api.mob(20000000002)
    assert response.ok


def test_mob_is_json():
    """
    Tests if an mob request returns JSON
    """
    api = test_garlandtools()
    response = api.mob(20000000002)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_mobs_is_ok():
    """
    Tests if an mobs request succeeds
    """
    api = test_garlandtools()
    response = api.mobs()
    assert response.ok


def test_mobs_is_json():
    """
    Tests if an mobs request returns JSON
    """
    api = test_garlandtools()
    response = api.mobs()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_node_is_ok():
    """
    Tests if an node request succeeds
    """
    api = test_garlandtools()
    response = api.node(153)
    assert response.ok


def test_node_is_json():
    """
    Tests if an node request returns JSON
    """
    api = test_garlandtools()
    response = api.node(153)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_nodes_is_ok():
    """
    Tests if an nodes request succeeds
    """
    api = test_garlandtools()
    response = api.nodes()
    assert response.ok


def test_nodes_is_json():
    """
    Tests if an nodes request returns JSON
    """
    api = test_garlandtools()
    response = api.nodes()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_npc_is_ok():
    """
    Tests if an npc request succeeds
    """
    api = test_garlandtools()
    response = api.npc(1000063)
    assert response.ok


def test_npc_is_json():
    """
    Tests if an npc request returns JSON
    """
    api = test_garlandtools()
    response = api.npc(1000063)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_npcs_is_ok():
    """
    Tests if an npcs request succeeds
    """
    api = test_garlandtools()
    response = api.npcs()
    assert response.ok


def test_npcs_is_json():
    """
    Tests if an npcs request returns JSON
    """
    api = test_garlandtools()
    response = api.npcs()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_quest_is_ok():
    """
    Tests if an quest request succeeds
    """
    api = test_garlandtools()
    response = api.quest(65537)
    assert response.ok


def test_quest_is_json():
    """
    Tests if an quest request returns JSON
    """
    api = test_garlandtools()
    response = api.quest(65537)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_quests_is_ok():
    """
    Tests if an quests request succeeds
    """
    api = test_garlandtools()
    response = api.quests()
    assert response.ok


def test_quests_is_json():
    """
    Tests if an quests request returns JSON
    """
    api = test_garlandtools()
    response = api.quests()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)

# -----------------------------------------------------------------------------


def test_search_is_ok():
    """
    Tests if an search request succeeds
    """
    api = test_garlandtools()
    response = api.search("Radiant")
    assert response.ok


def test_search_is_json():
    """
    Tests if an search request returns JSON
    """
    api = test_garlandtools()
    response = api.search("Radiant")
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, list)

# -----------------------------------------------------------------------------


def test_status_is_ok():
    """
    Tests if an status request succeeds
    """
    api = test_garlandtools()
    response = api.status(1)
    assert response.ok


def test_status_is_json():
    """
    Tests if an status request returns JSON
    """
    api = test_garlandtools()
    response = api.status(1)
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)


def test_statuses_is_ok():
    """
    Tests if an statuses request succeeds
    """
    api = test_garlandtools()
    response = api.statuses()
    assert response.ok


def test_statuses_is_json():
    """
    Tests if an statuses request returns JSON
    """
    api = test_garlandtools()
    response = api.statuses()
    assert response.ok

    response_json = response.json()
    assert isinstance(response_json, dict)
