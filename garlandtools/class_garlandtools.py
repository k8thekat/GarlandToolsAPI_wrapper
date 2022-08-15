# pylint: disable=line-too-long, too-many-public-methods
"""
Class definition: GarlandTools
Main API wrapper for GarlandTools.
"""

import requests_cache
from .globals import GARLAND_LANGUAGE_TOKEN, GARLAND_TOOLS_ACHIEVEMENT_ENDPOINT, GARLAND_TOOLS_ACHIEVEMENTS_ENDPOINT, GARLAND_TOOLS_DATA_ENDPOINT, GARLAND_TOOLS_LEVELLING_ENDPOINT, GARLAND_TOOLS_ENDGAME_GEAR_ENDPOINT, GARLAND_TOOLS_FATE_ENDPOINT, GARLAND_TOOLS_FATES_ENDPOINT, GARLAND_TOOLS_FISHING_ENDPOINT, GARLAND_TOOLS_ICON_ENDPOINT, GARLAND_TOOLS_INSTANCE_ENDPOINT, GARLAND_TOOLS_INSTANCES_ENDPOINT, GARLAND_TOOLS_ITEM_ENDPOINT, GARLAND_TOOLS_LEVE_ENDPOINT, GARLAND_TOOLS_LEVES_ENDPOINT, GARLAND_TOOLS_MAP_ENDPOINT, GARLAND_TOOLS_MOB_ENDPOINT, GARLAND_TOOLS_MOBS_ENDPOINT, GARLAND_TOOLS_NODE_ENDPOINT, GARLAND_TOOLS_NODES_ENDPOINT, GARLAND_TOOLS_NPC_ENDPOINT, GARLAND_TOOLS_NPCS_ENDPOINT, GARLAND_TOOLS_QUEST_ENDPOINT, GARLAND_TOOLS_QUESTS_ENDPOINT, GARLAND_TOOLS_SEARCH_ENDPOINT, GARLAND_TOOLS_STATUS_ENDPOINT, GARLAND_TOOLS_STATUSES_ENDPOINT
from .job import Job


class GarlandTools():
    """
    Main API wrapper for GarlandTools.
    """

    def __init__(self, cache_location="cache/garlandtools_cache", cache_expire_after=86400, language="en"):
        """
        Initialize the GarlandTools class.
        """
        self.cache_location = cache_location
        self.cache_expire_after = cache_expire_after
        self.language = language

        self.session = requests_cache.CachedSession(
            cache_location, backend='sqlite', expire_after=cache_expire_after)

    def achievement(self, achievement_id: int):
        """
        Returns an achievement by id
        """
        result = self.session.get(
            f'{GARLAND_TOOLS_ACHIEVEMENT_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}{achievement_id}.json')
        return result

    def achievements(self):
        """
        Returns all achievements
        """
        result = self.session.get(GARLAND_TOOLS_ACHIEVEMENTS_ENDPOINT.replace(
            GARLAND_LANGUAGE_TOKEN, self.language))
        return result

    def data(self):
        """
        Returns all core data
        """
        result = self.session.get(GARLAND_TOOLS_DATA_ENDPOINT.replace(
            GARLAND_LANGUAGE_TOKEN, self.language))
        return result

    def endgame_gear(self, job: Job):
        """
        Returns recommended endgame gear per job
        Use the common three letter abbreviation of the job.
        E.g.: White Mage => WHM; Warrior => WAR; Ninja => NIN
        """
        result = self.session.get(
            f'{GARLAND_TOOLS_ENDGAME_GEAR_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}{job}.json')
        return result

    def fate(self, fate_id: int):
        """
        Returns an fate by id
        """
        result = self.session.get(
            f'{GARLAND_TOOLS_FATE_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}{fate_id}.json')
        return result

    def fates(self):
        """
        Returns all fates
        """
        result = self.session.get(GARLAND_TOOLS_FATES_ENDPOINT.replace(
            GARLAND_LANGUAGE_TOKEN, self.language))
        return result

    def fishing(self):
        """
        Returns all fishing data
        """
        result = self.session.get(GARLAND_TOOLS_FISHING_ENDPOINT.replace(
            GARLAND_LANGUAGE_TOKEN, self.language))
        return result

    def icon(self, icon_type: str, icon_id: int):
        """
        Returns a specific icon by icon_type and icon_id
        """
        result = self.session.get(
            f'{GARLAND_TOOLS_ICON_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}{icon_type}/{icon_id}.png')
        return result

    def instance(self, instance_id: int):
        """
        Returns an instance by instance_id
        """
        result = self.session.get(
            f'{GARLAND_TOOLS_INSTANCE_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}{instance_id}.json')
        return result

    def instances(self):
        """
        Returns all instances
        """
        result = self.session.get(GARLAND_TOOLS_INSTANCES_ENDPOINT.replace(
            GARLAND_LANGUAGE_TOKEN, self.language))
        return result

    def item(self, item_id: int):
        """
        Returns a item by id

        Format: PNG
        """
        result = self.session.get(
            f'{GARLAND_TOOLS_ITEM_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}{item_id}.json')
        return result

    def leve(self, leve_id: int):
        """
        Returns an leve by id
        """
        result = self.session.get(
            f'{GARLAND_TOOLS_LEVE_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}{leve_id}.json')
        return result

    def leves(self):
        """
        Returns all leves
        """
        result = self.session.get(GARLAND_TOOLS_LEVES_ENDPOINT.replace(
            GARLAND_LANGUAGE_TOKEN, self.language))
        return result

    def leveling_gear(self, job: Job):
        """
        Returns levelling gear based on job
        """
        result = self.session.get(
            f'{GARLAND_TOOLS_LEVELLING_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}{job}.json')
        return result

    def map_zone(self, zone: str):
        """
        Returns a specific map by the zone.
        Some zones require the parent zone as well.
        E.g.: La Noscea/Lower La Noscea

        Format: PNG
        """
        result = self.session.get(
            f'{GARLAND_TOOLS_MAP_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}{zone}.png')
        return result

    def mob(self, mob_id: int):
        """
        Returns an mob by id
        """
        result = self.session.get(
            f'{GARLAND_TOOLS_MOB_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}{mob_id}.json')
        return result

    def mobs(self):
        """
        Returns all mobs
        """
        result = self.session.get(GARLAND_TOOLS_MOBS_ENDPOINT.replace(
            GARLAND_LANGUAGE_TOKEN, self.language))
        return result

    def node(self, node_id: int):
        """
        Returns an node by id
        """
        result = self.session.get(
            f'{GARLAND_TOOLS_NODE_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}{node_id}.json')
        return result

    def nodes(self):
        """
        Returns all nodes
        """
        result = self.session.get(GARLAND_TOOLS_NODES_ENDPOINT.replace(
            GARLAND_LANGUAGE_TOKEN, self.language))
        return result

    def npc(self, npc_id: int):
        """
        Returns an npc by id
        """
        result = self.session.get(
            f'{GARLAND_TOOLS_NPC_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}{npc_id}.json')
        return result

    def npcs(self):
        """
        Returns all npcs
        """
        result = self.session.get(GARLAND_TOOLS_NPCS_ENDPOINT.replace(
            GARLAND_LANGUAGE_TOKEN, self.language))
        return result

    def quest(self, quest_id: int):
        """
        Returns an quest by id
        """
        result = self.session.get(
            f'{GARLAND_TOOLS_QUEST_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}{quest_id}.json')
        return result

    def quests(self):
        """
        Returns all quests
        """
        result = self.session.get(GARLAND_TOOLS_QUESTS_ENDPOINT.replace(
            GARLAND_LANGUAGE_TOKEN, self.language))
        return result

    def search(self, query: str):
        """
        Submits a search query and returns the results
        """
        result = self.session.get(f'{GARLAND_TOOLS_SEARCH_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}'
                                  + f'?text={query}&lang={self.language}')
        return result

    def status(self, status_id: int):
        """
        Returns a status by id
        """
        result = self.session.get(
            f'{GARLAND_TOOLS_STATUS_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}{status_id}.json')
        return result

    def statuses(self):
        """
        Returns all statuses
        """
        result = self.session.get(
            f'{GARLAND_TOOLS_STATUSES_ENDPOINT.replace(GARLAND_LANGUAGE_TOKEN, self.language)}')
        return result
