# Async GarlandTools

Unofficial fork of the Python wrapper for [GarlandTools-PIP] API.  

__Notable Changes__:
- Overhauled response types to Typed Dicts
- Switched from `requests` to `aiohttp`.
    - Added `aiohttp_client_cache` to keep the features in line with the original [GarlandTools-PIP] project.
    - *note* - This cannot support/use an old cache object!.
- Created `Enums` for Language and Icon types to make it easier on the end user.
- Added support for using the class as a context manager. See [Usage](#usage)

---
__Replacing GarlandTools-PIP ?__

- Data is returned un-formatted unless mentioned otherwise to allow for an almost "drop-in" replacement from the [GarlandTools-PIP] library.
- They did not return the `JSON` payload and instead returned the raw `request.Session` object.
- All endpoint functions "should" overlap along with the parameters aside from one! (`icon`)


Special thanks to [GarlandTools] for providing this API and keeping it updated.

## Table of Contents

- [Installation](#installation)
- [Endpoints](#endpoints)
- [Usage](#usage)
- [Credits](#credits)
- [Changelog]

## Installation

`pip install async_garlandtools`

## Endpoints

All [GarlandTools] endpoints are implemented in this API.  
- All parameters asking for `*_id` are a an identifier from GarlandTools and or LamiaSheet.
- Some endpoint's support an `Enum`; such as "leveling_gear" and "endgame_gear".
- Some endpoint's return a generic `Object` class that houses response data as they return a `binary PNG` by default; see "map_zone" or "icon".


## Usage
To use the API, first initialize the `GarlandToolsAsync` class:
- The class supports context manager usage. (eg `async with`)
- You should be closing the `GarlandToolsASync` Sessions via `GarlandToolsAsync.close()` unless you provided your own.

**All Responses are TypedDicts outside of `map_zone` and `icon`.**


```python
from pathlib import Path

import aiohttp
from garlandtools import Job, IconType, Language, Object
# You can import the class however you want, but this is a drop in replacement via naming.
from garlandtools import GarlandToolsAsync as GarlandTools

if TYPE_CHECKING:
    from garlandtools._types import GearResponse, ItemResponse

# You can specify a cache location if you want.
# by default the cache location will be `Path(__file__).parent.joinpath("cache")`
cache_loc: Path = Path(__file__).parent.joinpath("cache")

# You can also change the language at any point via the `language` property.
# by default the language is `en`
lan = Language.English


# First will be used as a context manager.
async def context_sample() -> None:
    # Also supports providing your own `aiohttp.ClientSession`; 
    # but that will not allow the cache to be used unless you make a `CachedSession` object
    # from `aiohttp_client_cache.session`.
    async with GarlandTools(cache_location=cache_loc, language=lan) as garland_tools:
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
session = aiohttp.ClientSession()

# This is using the class NOT as a context manager.
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


```

All functions utilize a `aiohttp_client_cache` caching package ([aiohttp-cache]) which will create a local database of requests and only refresh after the cache is expired (default setting: 24h).  
[GarlandTools] only updates after patches usually.

## Credits

I want to credit [GarlandTools] and [GarlandTools-PIP] project for providing a starting point for me to learn.

[GTAsync]: GarlandToolsAsync
[GarlandTools]: garlandtools.org/
[GarlandTools-PIP]: https://github.com/SakulFlee/GarlandTools-PIP
[changelog]: https://github.com/k8thekat/GarlandToolsAPI_wrapper/blob/master/CHANGELOG.md
[aiohttp-cache]: https://pypi.org/project/aiohttp-client-cache/
