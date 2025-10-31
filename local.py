# type: ignore
# ruff: noqa
import contextlib
import argparse
import asyncio
import json
import logging
import subprocess
from argparse import Namespace
from configparser import ConfigParser
from logging import Logger
from pathlib import Path
from pprint import pformat, pprint
from time import time
from typing import TYPE_CHECKING, Any, ClassVar, Optional
from logging.handlers import TimedRotatingFileHandler
import datetime
import sys

import aiohttp
from async_garlandtools import Job, IconType, Language, Object
from async_garlandtools.errors import GarlandToolsKeyError
from async_garlandtools import GarlandToolsAsync as GarlandTools
from aiohttp_client_cache.session import CachedSession

if TYPE_CHECKING:
    from async_garlandtools._types import GearResponse, ItemResponse


local_data_path: Path = Path(__file__).parent.joinpath("")
response_path: Path = Path(__file__).parent.joinpath("garlandtools/_responses")
LOGGER: logging.Logger = logging.getLogger(__name__)


async def local_test() -> None:
    garland_tools = GarlandTools(cache_location=Path(__file__).parent)
    node_id = 9
    raise GarlandToolsKeyError("node", "node", node_id)
    # res = await garland_tools.item(8)
    # nodes = res["item"]["nodes"]
    # print(nodes)
    # # print(await garland_tools.node(197))
    # for node in nodes:
    #     print(node)
    #     print(await garland_tools.node(node))
    await garland_tools.close()
    pass


async def build() -> None:
    garland_tools = GarlandTools(cache_location=Path(__file__).parent)
    achievement = 19  # "Stick Them with the Pointy End I"
    res = await garland_tools.achievement(achievement)
    job = Job.WHITE_MAGE
    res = await garland_tools.endgame_gear(job)
    fate = 441  # "Harder, Bigger, Faster, Stronger",
    res = await garland_tools.fate(fate)
    icon_id = 2565  # Achievement, "To Crush Your Enemies IV"
    icon_type = IconType.achievement
    res = await garland_tools.icon(icon_id, icon_type)
    # https://www.garlandtools.org/files/icons/achievement/2565.png
    instance_id = 20027  # Urth's Fount
    res = await garland_tools.instance(instance_id)
    item_id = 10373
    res = await garland_tools.item(item_id)
    leve_id = 23  # "A Clogful of Camaraderie"
    res = await garland_tools.leve(leve_id)
    job = Job.DANCER
    res = await garland_tools.leveling_gear(job)
    zone = "La Noscea/Lower La Noscea"
    res = await garland_tools.map_zone(zone)
    mob_id = 18000000001446  # Gorgimera
    res = await garland_tools.mob(mob_id)
    node_id = 155  # Black Brush
    res = await garland_tools.node(node_id)
    npc_id = 1025610  # Gyotaku
    res = await garland_tools.npc(npc_id)
    quest_id = 69682  # Perfectly Awful
    res = await garland_tools.quest(quest_id)
    status_id = 2  # Stun
    res = await garland_tools.status(status_id)
    await garland_tools.close()


def ini_load(file: Path, section: str, options: list[str]) -> list[str | None]:
    """Parse an ini file.

    Parameters
    ----------
    file: :class:`Path`
        The file path.
    section: :class:`str`
        The name of the section. `[section_name]`.
    options: :class:`list[str]`
        The options to load as a list.

    Returns
    -------
        The list of options loaded in the same order.
    """
    if file.is_file():
        settings = ConfigParser(converters={"list": lambda setting: [value.strip() for value in setting.split(",")]})
        settings.read(filenames=file)
        res: list[str | None] = []
        for entry in options:
            res.append(settings.get(section=section, option=entry, fallback=None))
        return res
    else:
        raise FileNotFoundError("<%s> | Failed to load file. | Path: %s", "local.ini_load", file.as_posix())


def flatten(data: list, new_list: list) -> list:
    """Flatten a list."""
    for i in data:
        if isinstance(i, list):
            flatten(i, new_list)
        else:
            new_list.append(i)
    return new_list


def write_data_to_file(
    file_name: str,
    data: bytes | dict[Any, Any] | str | list,
    path: Path = Path(__file__).parent,
    *,
    mode: str = "w+",
    **kwargs: Any,
) -> None:
    """Basic file dump with json handling. If the data parameter is of type `dict`, `json.dumps()` will be used with an indent of 4.

    Parameters
    ----------
    path: :class:`Path`, optional
        The Path to write the data, default's to `Path(__file__).parent`.
    file_name: :class:`str`
        The name of the file, include the file extension.
    data: :class:`bytes | dict | str | list`
        The data to write out to the path and file_name provided.
    mode: :class:`str`, optional
        The mode to open the provided file path with using `<Path.open()>`.
    **kwargs: :class:`Any`
        Any additional kwargs to be supplied to `<json.dumps()>`, if applicable.

    """
    with path.joinpath(file_name).open(mode=mode) as file:
        LOGGER.debug("<%s.%s> | Wrote data to file %s located at: %s", __name__, "write_data_to_file", path, file_name)
        if isinstance(data, bytes):
            file.write(data.decode(encoding="utf-8"))
        elif isinstance(data, dict):
            file.write(json.dumps(data, indent=4, **kwargs))
        elif isinstance(data, list):
            if isinstance(data[0], dict):
                file.write(json.dumps(data, indent=4, **kwargs))
                return
            file.write("\n".join(data))
        else:
            file.write(data)
    LOGGER.info(
        "<%s.%s> | File write successful to path: %s ",
        __name__,
        "write_data_to_file",
        path.joinpath(file_name).as_posix(),
    )


class LogHandler:
    """
    Discord Multi-line code block formats:
    - https://github.com/highlightjs/highlight.js/blob/main/SUPPORTED_LANGUAGES.md

    """

    cur_log: Path
    code_formats: ClassVar[list[str]] = ["excel", "nc", "ml", " nim", " ps", " prolog", "thor"]
    default_code_format: str = "ps"

    def __init__(self, level: int = logging.INFO, local_dev: bool = True) -> None:
        self.path: Path = Path(__file__).parent.joinpath("logs")
        if self.path.exists() is False:
            self.path.mkdir()
        self.cur_log: Path = Path(__file__).parent.joinpath("logs/log.log")

        logging.basicConfig(
            level=level,
            format="%(asctime)s [%(threadName)s] [%(levelname)s]  %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p",
            handlers=[
                logging.StreamHandler(stream=sys.stdout),
                TimedRotatingFileHandler(
                    filename=Path.as_posix(self=self.path) + "/log.log",
                    when="midnight",
                    atTime=datetime.datetime.min.time(),
                    backupCount=4,
                    encoding="utf-8",
                    utc=True,
                ),
            ],
        )


class Launcher(Namespace):
    local: bool
    build: bool
    info: bool
    debug: bool
    upgrade: Optional[bool]


_parser = argparse.ArgumentParser(description="Local arg parse for Python Package development")
_parser.add_argument("-local", help="Run our local_test() function", default=False, required=False, action="store_true")
_parser.add_argument("-build", help="Run our development_text() function", default=False, required=False, action="store_true")
# uv sync -n --upgrade-package foo
_parser.add_argument("--upgrade", help="Run `uv sync -n --upgrade-package package_name`")
# If I want to add a group, this is what I use.
# group: argparse._MutuallyExclusiveGroup = _parser.add_mutually_exclusive_group(required=False)
_parser.add_argument("-info", help="Set the logging level to `INFO`.", default=False, required=False, action="store_true")
_parser.add_argument("-debug", help="Set the logging level to `INFO`.", default=False, required=False, action="store_true")
_parsed_args: Launcher = _parser.parse_known_args()[0]

# Logging section.
LOGGER.name = "Local Logging - "
if _parsed_args.info:
    LogHandler(level=logging.INFO)
elif _parsed_args.debug:
    LogHandler(level=logging.DEBUG)


# Any specific handling of launch args.
# Update `Launcher` class with new args and type def.
stime: float = time()
if _parsed_args.upgrade:
    LOGGER.info("Running uv sync upgrade. | Package: %s", _parsed_args.upgrade)
    subprocess.run(f"uv sync -n --upgrade-package {_parsed_args.upgrade}", check=False)  # noqa: S603
    LOGGER.info("Completed in %s seconds...", format(time() - stime, ".3f"))

if _parsed_args.local:
    LOGGER.info("Running local_test()...")
    with contextlib.suppress(KeyboardInterrupt, RuntimeError, asyncio.CancelledError):
        asyncio.run(local_test())
    LOGGER.info("Completed in %s seconds...", format(time() - stime, ".3f"))

if _parsed_args.build:
    LOGGER.info("Build...")
    with contextlib.suppress(KeyboardInterrupt, RuntimeError, asyncio.CancelledError):
        asyncio.run(build())
    LOGGER.info("Completed in %s seconds...", format(time() - stime, ".3f"))
