import logging
from pathlib import Path
from typing import TYPE_CHECKING

import aiohttp
from aiohttp_client_cache.session import CachedSession

from async_garlandtools import GarlandToolsAsync as GarlandTools, IconType, Job, Language, Object

if TYPE_CHECKING:
    from async_garlandtools._types import GearResponse, ItemResponse

local_data_path: Path = Path(__file__).parent
LOGGER: logging.Logger = logging.getLogger(__name__)
lan = Language.English
session = CachedSession()


# First will be as a context manager.
async def context_sample() -> None:
    # Also supports providing your own `aiohttp.ClientSession`;
    # but that will not allow the cache to be used unless you make a `CachedSession` object
    # from `aiohttp_client_cache.session`.
    async with GarlandTools(cache_location=local_data_path, language=lan) as garland_tools:
        job = Job.DANCER
        gear: GearResponse = await garland_tools.leveling_gear(job=job)
        # You can access any relevant information via dict keys.
        print(gear["equip"])
        item_id = 10373
        item: ItemResponse = await garland_tools.item(item_id=item_id)
        # You can access any relevant information via dict keys.
        print(item["item"], item["ingredients"])


# Also supports providing your own `aiohttp.ClientSession`;
# but that will not allow the cache to be used unless you make a `CachedSession` object
# from `aiohttp_client_cache.session`.
# session = aiohttp.ClientSession()


async def sample() -> None:
    # This GarlandTools object will not be able to cache as I provided an `aiohttp.ClientSession()`.
    garland_tools = GarlandTools(session=session)
    zone = "La Noscea/Lower La Noscea"
    map_resp: Object = await garland_tools.map_zone(zone)
    # Given `map_zone` used to return a binary PNG, that has been turned into a generic NamedTuple.
    # You can access the raw bytes via the `data` attribute.
    zone_raw: bytes = map_resp.data
    # Maybe you want the direct url, well here ya go.
    zone_url: str = map_resp.url
    # You can access the original `zone` parameter you passed into the function.
    zone_name: str = map_resp.zone

    # -------------------------------------------
    # Here is how to use the new `icon` endpoint.
    # https://www.garlandtools.org/files/icons/achievement/2565.png
    icon_id = 2565  # Achievement, "To Crush Your Enemies IV"
    icon_type = IconType.achievement
    # You have access to the same attributes as before as it's another `Object`.
    icon_resp: Object = await garland_tools.icon(icon_id, icon_type)
    # We also provide the original Enum to the response object for ease via `icon_type`.
    print(icon_resp.url, icon_resp.icon_type)

    # Since I provided my own `aiohttp.ClientSession()` I can either close it here via..
    await garland_tools.close()
    # or leave it open if I am using the Session elsewhere.
