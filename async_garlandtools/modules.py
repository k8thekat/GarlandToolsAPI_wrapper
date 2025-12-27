"""Copyright (C) 2021-2025 Katelynn Cadwallader.

This file is part of GarlandToolsAPI_wrapper.

GarlandToolsAPI_wrapper is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3, or (at your option)
any later version.

GarlandToolsAPI_wrapper is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
License for more details.

You should have received a copy of the GNU General Public License
along with GarlandToolsAPI_wrapper; see the file COPYING.  If not, write to the Free
Software Foundation, 51 Franklin Street - Fifth Floor, Boston, MA
02110-1301, USA.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal, NamedTuple, Optional, Self, overload

from aiohttp.client_exceptions import ContentTypeError
from aiohttp_client_cache import SQLiteBackend
from aiohttp_client_cache.session import CachedSession

from ._enums import Language
from .errors import *

if TYPE_CHECKING:
    import datetime
    import types

    import aiohttp
    from aiohttp.client import _RequestOptions as AiohttpRequestOptions  # pyright: ignore[reportPrivateUsage]

    from ._enums import IconType, Job
    from ._types import *

    ResponseDataAlias = Union[
        LeveResponse,
        DataResponse,
        MultiPartResponse,
        GearResponse,
        InstanceResponse,
        AchievementResponse,
        FateResponse,
        ItemResponse,
        MobResponse,
        NodeResponse,
        NPCResponse,
        QuestResponse,
        StatusResponse,
        list[SearchResponse],
    ]

LOGGER = logging.getLogger(__name__)


ENDPOINT = "https://www.garlandtools.org/"
LANGUAGE = "LANGUAGE"

ACHIEVEMENT_ENDPOINT = f"{ENDPOINT}db/doc/achievement/LANGUAGE/2/"
ACHIEVEMENTS_ENDPOINT = f"{ENDPOINT}db/doc/browse/LANGUAGE/2/achievement.json"

DATA_ENDPOINT = f"{ENDPOINT}db/doc/core/LANGUAGE/3/data.json"

LEVELLING_ENDPOINT = f"{ENDPOINT}db/doc/equip/LANGUAGE/2/leveling-"
ENDGAME_GEAR_ENDPOINT = f"{ENDPOINT}db/doc/equip/LANGUAGE/2/end-"

FATE_ENDPOINT = f"{ENDPOINT}db/doc/fate/LANGUAGE/2/"
FATES_ENDPOINT = f"{ENDPOINT}db/doc/browse/LANGUAGE/2/fate.json"

FISHING_ENDPOINT = f"{ENDPOINT}db/doc/browse/LANGUAGE/2/fishing.json"

ICON_ENDPOINT = f"{ENDPOINT}files/icons/"

INSTANCE_ENDPOINT = f"{ENDPOINT}db/doc/instance/LANGUAGE/2/"
INSTANCES_ENDPOINT = f"{ENDPOINT}db/doc/browse/LANGUAGE/2/instance.json"

ITEM_ENDPOINT = f"{ENDPOINT}db/doc/item/LANGUAGE/3/"

LEVE_ENDPOINT = f"{ENDPOINT}db/doc/leve/LANGUAGE/3/"
LEVES_ENDPOINT = f"{ENDPOINT}db/doc/browse/LANGUAGE/2/leve.json"

MAP_ENDPOINT = f"{ENDPOINT}files/maps/"

MOB_ENDPOINT = f"{ENDPOINT}db/doc/mob/LANGUAGE/2/"
MOBS_ENDPOINT = f"{ENDPOINT}db/doc/browse/LANGUAGE/2/mob.json"

NODE_ENDPOINT = f"{ENDPOINT}db/doc/node/LANGUAGE/2/"
NODES_ENDPOINT = f"{ENDPOINT}db/doc/browse/LANGUAGE/2/node.json"

NPC_ENDPOINT = f"{ENDPOINT}db/doc/npc/LANGUAGE/2/"
NPCS_ENDPOINT = f"{ENDPOINT}db/doc/browse/LANGUAGE/2/npc.json"

QUEST_ENDPOINT = f"{ENDPOINT}db/doc/quest/LANGUAGE/2/"
QUESTS_ENDPOINT = f"{ENDPOINT}db/doc/browse/LANGUAGE/2/quest.json"

SEARCH_ENDPOINT = f"{ENDPOINT}api/search.php"

STATUS_ENDPOINT = f"{ENDPOINT}db/doc/Status/LANGUAGE/2/"
STATUSES_ENDPOINT = f"{ENDPOINT}db/doc/browse/LANGUAGE/2/status.json"


__all__ = ["GarlandToolsAsync", "Object"]


class Object(NamedTuple):
    """Represents the data returned from any function that returns a "picture".

    Attributes
    ----------
    url: :class:`str`
        The GarlandTools.org url.
    data: :class:`bytes`
        The raw bytes
    zone: :class:`Optional[str]`, optional
        The name of the Zone if applicable, default is None.
    icon_type: :class:`Optional[IconType]`, optional
        The category the icon belongs to if applicable, default is None.

    """

    url: str
    "The GarlandTools URL"
    data: bytes
    "A representation of the data raw."
    zone: Optional[str] = None
    "The name of the Zone, if applicable."
    icon_type: Optional[IconType] = None
    "The IconType, if applicable."


class GarlandToolsAsync:
    """An `async` version of the GarlandTools API.

    Supports context manager `async with` functionality.
    """

    _session: aiohttp.ClientSession | CachedSession
    _language: Language
    _cache: SQLiteBackend

    def __init__(
        self,
        *,
        session: Optional[aiohttp.ClientSession | CachedSession] = None,
        cache_location: Optional[Path] = None,
        cache_expire_after: datetime.datetime | int | datetime.timedelta = 172800,
        language: str | Language = Language.English,
    ) -> None:
        """Build your GarlandToolsAsync class.

        .. note::
            If you provide your own `aiohttp.ClientSession` the information will no longer be cached.


        .. warning::
            Unless the `session` parameter is a `aiohttp_client_cache.session.CachedSession`, caching will be disabled.



        Parameters
        ----------
        session: :class:`Optional[aiohttp.ClientSession | CachedSession]`, optional
            An existing :class:`aiohttp.ClientSession` or :class:`CachedSession` object otherwise :class:`GarlandToolsAsync`
            will open a :class:`CachedSession`, by default None.
        cache_location: :class:`Path`, optional
            The location to store the request cache, by default "Path(__file__).parent/cache/".
            - Do not include a file name.
        cache_expire_after: :class:`datetime | timedelta | int`, optional
            How long until the cache expires in seconds, by default 172800. (Roughly every other day)
        language: :class:`str` | :class:`Language`, optional
            The language for API queries, by default "en".
            - Can be changed via the `language` property.

        Raises
        ------
        NotADirectoryError
            If the parameter `cache_location` is not a directory.

        """
        if isinstance(language, str):
            for idx in Language._member_names_:
                if idx.lower().startswith(language.lower()):
                    self.language = Language(value=language.lower())
                    LOGGER.warning(
                        (
                            "<%s.__init__> | Found a string version of parameter `language` instead of the <Language(Enum)> class, "
                            "attempting to map. | results: %s"
                        ),
                        __class__.__name__,
                        self.language,
                    )
                    break
                self.language = Language.English
        else:
            self.language = language

        # This handles local cache building.
        if session is None:
            if cache_location is None:
                cache_location = Path(__file__).parent.joinpath("cache")

            if cache_location.exists() is False:
                cache_location.mkdir()

            elif cache_location.is_dir() is False:
                msg = "<%s> | File Path provided is not a directory. | Path: %s"
                raise NotADirectoryError(msg, __class__.__name__, cache_location)

            _cache = SQLiteBackend(
                cache_name=cache_location.joinpath("garlandtools_cache").as_posix(),
                autoclose=True,
                expire_after=cache_expire_after,
            )
            self._session = CachedSession(cache=_cache)
            return

        if isinstance(session, CachedSession):
            self._session = session
            return

        self._session = session

    @property
    def language(self) -> Language:
        """Set the language for the API queries."""
        return self._language

    @language.setter
    def language(self, value: Language) -> None:
        self._language = value

    @property
    def session(self) -> aiohttp.ClientSession | CachedSession:
        """The local `aiohttp.ClientSession` or `CachedSession` object."""
        return self._session

    async def close(self) -> None:
        """Closes any open resources."""
        LOGGER.debug("<%s._close()> | Closing open `%s` %s", __class__.__name__, type(self.session), self.session)
        await self.session.close()

    async def __aexit__(  # noqa: D105
        self,
        exc_type: Optional[type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[types.TracebackType],
    ) -> None:
        await self.close()

    async def __aenter__(self) -> Self:  # noqa: D105
        return self

    @overload
    async def _request(
        self,
        url: str,
        *,
        content_only: Literal[True],
        request_params: Optional[AiohttpRequestOptions] = ...,
    ) -> bytes | Any: ...

    @overload
    async def _request(
        self,
        url: str,
        *,
        content_only: bool = False,
        request_params: Optional[AiohttpRequestOptions] = ...,
    ) -> ResponseDataAlias | Any: ...

    async def _request(
        self,
        url: str,
        *,
        content_only: bool = False,
        request_params: Optional[AiohttpRequestOptions] = None,
    ) -> ResponseDataAlias | Any:
        LOGGER.debug(
            "<%s._request> | url: %s | session: %s | request_params: %s ",
            __class__.__name__,
            url,
            self.session,
            request_params,
        )


        # If the user supplied session is None; we create our own and set it to a private
        # attribute so we can close it later, otherwise we will use the user supplied session.
        # kwargs handler.
        if request_params is None:
            data: aiohttp.ClientResponse = await self.session.get(url=url)
        else:
            data = await self.session.get(url=url, **request_params)

        LOGGER.debug("<%s._request> | Status Code: %s | Content Type: %s", __class__.__name__, data.status, data.content_type)
        if not 200 <= data.status < 300:
            raise GarlandToolsRequestError(data.status, url, "generic http request")
        if data.status == 400:
            raise GarlandToolsRequestError(
                data.status,
                url,
                "invalid parameters",
            )
        if data.status == 404:
            raise GarlandToolsRequestError(
                data.status,
                url,
                "invalid http request",
            )

        # Currently used by icon and map_zone function.
        if content_only:
            content = await data.content.read()
            LOGGER.debug("<%s._request> | Data: %s", __class__.__name__, content)
            return content
        # If for any reason JSON parsing is failing, we will raise an exception.
        try:
            res: Any = await data.json()
        except ContentTypeError:
            raise GarlandToolsTypeError(func="request", cur_type=data.content_type, expec_type="application/json") from None

        LOGGER.debug("<%s._request> | Data: %s", __class__.__name__, res)
        return res

    async def achievement(self, achievement_id: int) -> AchievementResponse:
        """Returns an Achievement by ID.

        Parameters
        ----------
        achievement_id: :class:`int`
            The Final Fantasy 14 Achievement ID.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "achievement" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`AchievementResponse`
            The response data in JSON format with an "achievement" key housing the related data.

        """
        result: ResponseDataAlias = await self._request(
            f"{ACHIEVEMENT_ENDPOINT.replace(LANGUAGE, self.language.value)}{achievement_id}.json",
        )
        # if not ("quest" in result and "partials" in result) or isinstance(result, list):
        if "achievement" not in result or isinstance(result, list):
            raise GarlandToolsKeyError("achievement", "achievement", achievement_id)  # noqa: EM101 # The message is being assigned and built in the class __init__.
        return result

    async def achievements(self) -> list[PartialIndex]:
        """Returns all Achievement's.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "browse" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`list[PartialIndex]`
            The response data in JSON format as a list of partial keys related to information about each Achievement.

        """
        result: ResponseDataAlias = await self._request(ACHIEVEMENTS_ENDPOINT.replace(LANGUAGE, self.language.value))
        if "browse" not in result or isinstance(result, list):
            raise GarlandToolsKeyError(key_name="browse", func="achievements")
        return result["browse"]

    async def data(self) -> DataResponse:
        """Returns all core GarlandTools data.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "achievementCategoryIndex" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.


        Returns
        -------
        :class:`DataResponse`
            The response data in JSON format with multiple keys housing
            information about Jobs, Ventures, Quests, Locations, Nodes, etc...

        """
        result: ResponseDataAlias = await self._request(DATA_ENDPOINT.replace(LANGUAGE, self.language.value))
        if "achievementCategoryIndex" not in result or isinstance(result, list):
            raise GarlandToolsKeyError(key_name="achievementCategoryIndex", func="data")
        return result

    async def endgame_gear(self, job: Job) -> GearResponse:
        """Returns recommended endgame gear per job.

        ---
        **Equipment Slots**
        - Main Hand = 1
        - Off Hand = 2
        - Head = 3
        - Chest = 4
        - Hands = 5
        - Legs = 7
        - Feet = 8
        - Earrings = 9
        - Necklace = 10
        - Bracelets = 11
        - Ring = 12
        - MainHand Only / Two-Handed = 13

        Parameters
        ----------
        job: :class:`Job`
            The Final Fantasy 14 Job you want to look up.


        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "equip" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`GearResponse`
            The response data in JSON format with multiple keys housing information related to the job provided.
            - The partials key has basic information related to the Item IDs provided. (Name, ilvl)
            - The key number correlates to the equipment slot, see above.

        """
        result: ResponseDataAlias = await self._request(f"{ENDGAME_GEAR_ENDPOINT.replace(LANGUAGE, self.language.value)}{job.value}.json")
        if "equip" not in result or isinstance(result, list):
            raise GarlandToolsKeyError("equip", "endgame_gear", job)  # noqa: EM101 # The message is being assigned and built in the class __init__.
        return result

    async def fate(self, fate_id: int) -> FateResponse:
        """Returns a Fate by ID.

        Parameters
        ----------
        fate_id: :class:`int`
            The Final Fantasy 14 Fate ID.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "fate" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`FateResponse`
            The response data in JSON format with the "fate" key housing the related data.

        """
        result: ResponseDataAlias = await self._request(f"{FATE_ENDPOINT.replace(LANGUAGE, self.language.value)}{fate_id}.json")
        if "fate" not in result or isinstance(result, list):
            raise GarlandToolsKeyError("fate", "fate", fate_id)  # noqa: EM101 # The message is being assigned and built in the class __init__.
        return result

    async def fates(self) -> list[PartialIndex]:
        """Returns all Fates.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "browse" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`list[PartialIndex]`
            The response data in JSON format as a list of partial keys related to information about each Fate.

        """
        result: ResponseDataAlias = await self._request(FATES_ENDPOINT.replace(LANGUAGE, self.language.value))
        if "browse" not in result or isinstance(result, list):
            raise GarlandToolsKeyError(key_name="browse", func="achievements")
        return result["browse"]

    async def fishing(self) -> list[PartialIndex]:
        """Returns all Fishing spot data.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "browse" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`list[PartialIndex]`
            The response data in JSON format as a list of partial keys related to information about each Fishing Spot.

        """
        result: ResponseDataAlias = await self._request(FISHING_ENDPOINT.replace(LANGUAGE, self.language.value))
        if "browse" not in result or isinstance(result, list):
            raise GarlandToolsKeyError(key_name="browse", func="achievements")
        return result["browse"]

    async def icon(
        self,
        icon_id: int,
        icon_type: IconType,
        *,
        thumbnail: bool = True,
        content_only: bool = True,
        **params: Optional[AiohttpRequestOptions],
    ) -> Object:
        """Returns a specific icon by icon_type and icon_id.

        .. note::
            Typically the `icon_type` parameter will be related to the category. This can be deduced from the URL.
            - Example: `www.garlandtools.org/db/doc/fate/en/2/441.json` -> `.../doc/{category}/{language}/2/{id}.json`

        .. warning::
            Setting `thumbnail` to False can result in a `404` error due to an invalid URL.

        Parameters
        ----------
        icon_id: :class:`int`
            The ID of the icon. An example would be an "item" ID.
        icon_type: :class:`IconType`
            The type or category of icon the `icon_id` belongs to.
        thumbnail: :class:`bool`, optional
            If you want a lower resolution icon image, by default is `True`
            - Not all Icons have a high resolution image, so having this on by default guarantees a result(typically).
        content_only: :class:`bool`, optional
            A flag that causes our `self._request` function to only return raw `bytes`
            data instead of JSON or similar, by default is `True`.
        **params: :class:`Optional[AiohttpRequestOptions]`
            Any key-word parameters to supply to our :class:`aiohttp.ClientResponse` object.

        Raises
        ------
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`Object`
            A generic object to house the response content with the url.

        """
        url = f"{ICON_ENDPOINT.replace(LANGUAGE, self.language.value)}{icon_type.name}/t/{icon_id}.png"
        if thumbnail is False:
            url = f"{ICON_ENDPOINT.replace(LANGUAGE, self.language.value)}{icon_type.name}/{icon_id}.png"
        result: bytes | Any = await self._request(url, content_only=content_only, **params)
        return Object(icon_type=icon_type, url=url, data=result)

    async def instance(self, instance_id: int) -> InstanceResponse:
        """Returns a Instance by ID.

        Parameters
        ----------
        instance_id: :class:`int`
            The Final Fantasy 14 Instance ID.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "instance" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`InstanceResponse`
            The response data in JSON format with an "instance" key housing the related data.

        """
        result: ResponseDataAlias = await self._request(f"{INSTANCE_ENDPOINT.replace(LANGUAGE, self.language.value)}{instance_id}.json")
        if "instance" not in result or isinstance(result, list):
            raise GarlandToolsKeyError("instance", "instance", instance_id)  # noqa: EM101 # The message is being assigned and built in the class __init__.
        return result

    async def instances(self) -> list[PartialIndex]:
        """Returns all Instances.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "browse" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`list[PartialIndex]`
            The response data in JSON format as a list of partial keys related to information about each Instance.

        """
        result: ResponseDataAlias = await self._request(INSTANCES_ENDPOINT.replace(LANGUAGE, self.language.value))
        if "browse" not in result or isinstance(result, list):
            raise GarlandToolsKeyError(key_name="browse", func="instances")
        return result["browse"]

    async def item(self, item_id: int | str) -> ItemResponse:
        """Returns a Item by ID.

        Parameters
        ----------
        item_id: :class:`int | str`
            The Final Fantasy 14 Item ID.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "item" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`ItemResponse`
            The response data in JSON format with the keys "item", "ingredients" and "partials" housing the related data.

        """
        result: ResponseDataAlias = await self._request(f"{ITEM_ENDPOINT.replace(LANGUAGE, self.language.value)}{item_id}.json")
        if "item" not in result or "voyages" in result or isinstance(result, list):
            raise GarlandToolsKeyError("item", "item", item_id)  # noqa: EM101 # The message is being assigned and built in the class __init__.
        return result

    async def leve(self, leve_id: int) -> LeveResponse:
        """Returns a Leve by ID.

        Parameters
        ----------
        leve_id: :class:`int`
            The Final Fantasy 14 Leve ID.

        Returns
        -------
        :class:`LeveResponse`
            The response data in JSON format with the keys "leve", "ingredients", "rewards" and "partials" housing the related data.

        """
        result: ResponseDataAlias = await self._request(f"{LEVE_ENDPOINT.replace(LANGUAGE, self.language.value)}{leve_id}.json")
        if "leve" not in result or isinstance(result, list):
            raise GarlandToolsKeyError("leve", "leve", leve_id)  # noqa: EM101 # The message is being assigned and built in the class __init__.
        return result

    async def leves(self) -> list[PartialIndex]:
        """Returns all Leve's.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "browse" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`list[PartialIndex]`
            The response data in JSON format as a list of partial keys related to information about each Leve.

        """
        result: ResponseDataAlias = await self._request(LEVES_ENDPOINT.replace(LANGUAGE, self.language.value))
        if "browse" not in result or isinstance(result, list):
            raise GarlandToolsKeyError(key_name="browse", func="instances")
        return result["browse"]

    async def leveling_gear(self, job: Job) -> GearResponse:
        """Returns leveling gear based on Job.

        Parameters
        ----------
        job: :class:`Job`
            The Final Fantasy 14 Job you want to look up.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "equip" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`GearResponse`
            The response data in JSON format with the keys "equip" and "partials" housing the related data.

        """
        result: ResponseDataAlias = await self._request(f"{LEVELLING_ENDPOINT.replace(LANGUAGE, self.language.value)}{job.value}.json")
        if "equip" not in result or isinstance(result, list):
            raise GarlandToolsKeyError("equip", "leveling_gear", job)  # noqa: EM101 # The message is being assigned and built in the class __init__.
        return result

    async def map_zone(self, zone: str) -> Object:
        """Returns a specific map by the zone.

        .. note::
            Some zones require the parent zone as well.
            E.g.: La Noscea/Lower La Noscea

        Parameters
        ----------
        zone: :class:`str`
            The zone name.

        Raises
        ------
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`Object`
            A generic object housing the URL and data as bytes.

        """
        url: str = f"{MAP_ENDPOINT.replace(LANGUAGE, self.language.value)}{zone}.png"
        result: bytes | Any = await self._request(url, content_only=True)
        return Object(url=url, data=result, zone=zone)

    async def mob(self, mob_id: int) -> MobResponse:
        """Returns a Mob by ID.

        Parameters
        ----------
        mob_id: :class:`int`
            The Final Fantasy 14 monster ID.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "mob" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`MobResponse`
            The response data in JSON format with the "mob" key housing the related data.

        """
        result: ResponseDataAlias = await self._request(f"{MOB_ENDPOINT.replace(LANGUAGE, self.language.value)}{mob_id}.json")
        if "mob" not in result or isinstance(result, list):
            raise GarlandToolsKeyError("mob", "mob", mob_id)  # noqa: EM101 # The message is being assigned and built in the class __init__.
        return result

    async def mobs(self) -> list[PartialIndex]:
        """Returns all mobs.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "browse" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`list[PartialIndex]`
            The response data in JSON format as a list of partial keys related to information about each Mob.

        """
        result: ResponseDataAlias = await self._request(MOBS_ENDPOINT.replace(LANGUAGE, self.language.value))
        if "browse" not in result or isinstance(result, list):
            raise GarlandToolsKeyError(key_name="browse", func="instances")
        return result["browse"]

    async def node(self, node_id: int) -> NodeResponse:
        """Returns a Gatherable Node by ID.

        Parameters
        ----------
        node_id: :class:`int`
            The Gatherable Node ID.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "node" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`NodeResponse`
            The response data in JSON format with the keys "node" and "partials" housing the related data.

        """
        result: ResponseDataAlias = await self._request(f"{NODE_ENDPOINT.replace(LANGUAGE, self.language.value)}{node_id}.json")
        if "node" not in result or isinstance(result, list):
            # if "node" not in result and "partials" not in result:
            raise GarlandToolsKeyError("node", "node", node_id)  # noqa: EM101 # The message is being assigned and built in the class __init__.
        return result

    async def nodes(self) -> list[PartialIndex]:
        """Returns all Nodes.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "browse" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`list[PartialIndex]`
            The response data in JSON format as a list of partial keys related to information about each Node.

        """
        result: ResponseDataAlias = await self._request(NODES_ENDPOINT.replace(LANGUAGE, self.language.value))
        if "browse" not in result or isinstance(result, list):
            raise GarlandToolsKeyError(key_name="browse", func="nodes")
        return result["browse"]

    async def npc(self, npc_id: int) -> NPCResponse:
        """Returns a NPC by ID.

        Parameters
        ----------
        npc_id: :class:`int`
            The NPC ID.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "npc" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`NPCResponse`
            The response data in JSON format with the key "npc" housing the related data.

        """
        result: ResponseDataAlias = await self._request(f"{NPC_ENDPOINT.replace(LANGUAGE, self.language.value)}{npc_id}.json")
        if "npc" not in result or isinstance(result, list):
            raise GarlandToolsKeyError("npc", "npc", npc_id)  # noqa: EM101 # The message is being assigned and built in the class __init__.
        return result

    async def npcs(self) -> list[PartialIndex]:
        """Returns all NPC's.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "browse" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`list[PartialIndex]`
            The response data in JSON format as a list of partial keys related to information about each NPC.

        """
        result: ResponseDataAlias = await self._request(NPCS_ENDPOINT.replace(LANGUAGE, self.language.value))
        if "browse" not in result or isinstance(result, list):
            raise GarlandToolsKeyError(key_name="browse", func="nodes")
        return result["browse"]

    async def quest(self, quest_id: int) -> QuestResponse:
        """Returns a Quest by ID.

        Parameters
        ----------
        quest_id: :class:`int`
            The Final Fantasy 14 Quest ID.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "quest" key and "partials" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`QuestResponse`
            The response data in JSON format with the keys "quests" and "partials" housing the related data.

        """
        result: ResponseDataAlias = await self._request(f"{QUEST_ENDPOINT.replace(LANGUAGE, self.language.value)}{quest_id}.json")
        if not ("quest" in result and "partials" in result) or isinstance(result, list):
            raise GarlandToolsKeyError("quest", "quest", quest_id)  # noqa: EM101 # The message is being assigned and built in the class __init__.
        return result

    async def quests(self) -> list[PartialIndex]:
        """Returns all Quest's.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "browse" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`list[PartialIndex]`
            The response data in JSON format as a list of partial keys related to information about each Quest.

        """
        result: ResponseDataAlias = await self._request(QUESTS_ENDPOINT.replace(LANGUAGE, self.language.value))
        if "browse" not in result or isinstance(result, list):
            raise GarlandToolsKeyError(key_name="browse", func="nodes")
        return result["browse"]

    async def search(self, query: str) -> list[SearchResponse]:
        """Submits a search query and returns the results.

        Parameters
        ----------
        query: :class:`str`
            The string to search for.

        Raises
        ------
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format, or of the response is not a :class:`list`.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`list[SearchResponse]`
            The response data in JSON format as a list of partial matches related to your search,
            containing the keys "type", "id" and "obj".

        """
        result: ResponseDataAlias = await self._request(
            f"{SEARCH_ENDPOINT.replace(LANGUAGE, self.language.value)}?text={query}&lang={self.language.value}",
        )
        if not isinstance(result, list):
            raise GarlandToolsTypeError(func="search", cur_type=type(result), expec_type=list)
        return result

    async def status(self, status_id: int) -> StatusResponse:
        """Return a Status by ID.

        Parameters
        ----------
        status_id: :class:`int`
            The Final Fantasy 14 Status ID.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "status" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`StatusResponse`
            The response data in JSON format with the key "status" housing the related data.

        """
        result: ResponseDataAlias = await self._request(f"{STATUS_ENDPOINT.replace(LANGUAGE, self.language.value)}{status_id}.json")
        if "status" not in result or isinstance(result, list):
            raise GarlandToolsKeyError("status", "status", status_id)  # noqa: EM101 # The message is being assigned and built in the class __init__.
        return result

    async def statuses(self) -> list[PartialIndex]:
        """Returns all Statuses.

        Raises
        ------
        :class:`GarlandToolsKeyError`
            If the "browse" key is not found in the response data.
        :class:`GarlandToolsTypeError`
            If the response data is not in JSON format.
        :class:`GarlandToolsRequestError`
            If the status code is not 200.

        Returns
        -------
        :class:`list[PartialIndex]`
            The response data in JSON format as a list of partial keys related to information about each Status.

        """
        result: ResponseDataAlias = await self._request(f"{STATUSES_ENDPOINT.replace(LANGUAGE, self.language.value)}")
        if "browse" not in result or isinstance(result, list):
            raise GarlandToolsKeyError(key_name="browse", func="statuses")
        return result["browse"]
