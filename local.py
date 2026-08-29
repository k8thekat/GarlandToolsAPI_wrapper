# pyright: ignore[reportUnusedImport]  # noqa: D100
from __future__ import annotations

import argparse
import asyncio
import contextlib
import datetime
import inspect
import json
import logging
import subprocess
import sys
from argparse import Namespace
from configparser import ConfigParser
from json import JSONEncoder
from logging import Logger
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from pprint import pformat, pprint
from time import time
from typing import TYPE_CHECKING, Any, ClassVar, NotRequired, Optional, TypedDict, Union, Unpack

import aiohttp
import asqlite
from async_garlandtools import Job, IconType, Language, Object
from async_garlandtools.errors import GarlandToolsKeyError
from async_garlandtools import GarlandToolsAsync as GarlandTools
from aiohttp_client_cache.session import CachedSession

if TYPE_CHECKING:
    import sqlite3
    from collections.abc import Callable, Coroutine, Iterable
    from async_garlandtools._types import GearResponse, ItemResponse


LOCAL_DATA_PATH: Path = Path(__file__).parent.joinpath("local_data")
RESPONSE_PATH: Path = Path(__file__).parent.joinpath("_responses")
LOGGER: logging.Logger = logging.getLogger(__name__)
TIMESTAMP_FORMAT = "%d/%m | %H:%M(%Z)"


class DumpParameters(TypedDict, total=False):
    skipkeys: bool
    ensure_ascii: bool
    check_circular: bool
    allow_nan: bool
    cls: type[JSONEncoder] | None
    indent: None | int | str
    separators: tuple[str, str] | None
    default: Callable[[Any], Any] | None
    sort_keys: bool


class WriteDataParametersPartial(DumpParameters):
    file_name: str
    data: NotRequired[bytes | dict[Any, Any] | str | list[str]]
    path: Path
    mode: NotRequired[str]


class WriteDataParameters(DumpParameters):  # noqa: D101
    file_name: str
    data: bytes | dict[Any, Any] | str | list[str]
    path: Path
    mode: str


async def local_test() -> None:
    garland_tools = GarlandTools(cache_location=LOCAL_DATA_PATH)
    npc_id = 1016902  # Dreamer Egg NPC
    icon_id = 38316
    data = await garland_tools.icon(npc_id)
    print(data)
    # res = await garland_tools.item(8)
    # nodes = res["item"]["nodes"]

    # print(nodes)
    # # print(await garland_tools.node(197))
    # for node in nodes:
    #     print(node)
    #     print(await garland_tools.node(node))
    Local.write_data_to_file(file_name="npc.json", data=data, path=RESPONSE_PATH)
    await garland_tools.close()


async def build() -> None:
    garland_tools = GarlandTools(cache_location=LOCAL_DATA_PATH)
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


class Local:
    """Local class housing useful functionality."""

    async def request(  # noqa: D102
        self,
        url: str,
        session: Optional[aiohttp.ClientSession] = None,
        auto_close: bool = True,
        raw_bytes: bool = False,
    ) -> Optional[bytes | dict[Any, Any]]:  # pyright: ignore[reportUnusedFunction]
        if session is None:
            session = aiohttp.ClientSession()

        res: aiohttp.ClientResponse = await session.get(url=url)
        if res.status != 200:
            LOGGER.error("<%s._request> failed to access the url. | Status Code: %s | URL: %s", __file__, res.status, url)
            return None
            # raise ConnectionError("Unable to access the url: %s", url)
        if raw_bytes:
            data = await res.content.read()
        else:
            data = await res.json()
        if auto_close:
            await session.close()
        return data

    async def time_validation(self, func: Callable[..., Coroutine[Any, Any, Any]]) -> Any:
        stime = time()
        if inspect.iscoroutinefunction(func):
            var = await func()
        else:
            var = func()

        LOGGER.info("Completed local_test() in %s seconds...", format(time() - stime, ".3f"))
        return var

    def ini_load(self, file: Path, section: str, options: list[str]) -> list[str | None]:
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
        msg = f"<local.ini_load> | Failed to load file. | Path: {file.as_posix()}"
        raise FileNotFoundError(msg)

    def flatten(self, data: Iterable[Any], new_list: list[Any]) -> list[Any]:
        """Flatten a list."""
        for i in data:
            if isinstance(i, list):
                self.flatten(i, new_list)
            else:
                new_list.append(i)
        return new_list

    def load_data_from_file(
        self,
        path: Path,
        size: Optional[int] = None,
        is_json: bool = False,
        encoding: str = "utf-8",
    ) -> str | dict[Any, Any]:
        """Basic file read.

        Parameters
        ----------
        path: :class:`Path`
            The Path to load the data from.
        size: :class:`Optional[int]`, optional
            The amount of data to read if needed, by default None will read until EOF.

        Returns
        -------
        :class:`str`
            The file data.

        Raises
        ------
        FileNotFoundError
            If the file path doesn't exist.

        """
        if path.exists() is False:
            msg = "<%s.%s> | The Path provided does not exist. | Path: %s"
            raise FileNotFoundError(msg, __name__, "load_data_from_file", path)

        with path.open(mode="r", encoding=encoding) as file:
            if is_json is True:
                return json.loads(file.read(size))
            return file.read(size)

    @staticmethod
    def write_data_to_file(
        file_name: str,
        data: bytes | dict[Any, Any] | str | list,
        path: Path = Path(__file__).parent,
        *,
        mode: str = "w+",
        **kwargs: Unpack[DumpParameters],
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
        if kwargs.get("indent") is None:
            kwargs["indent"] = 4

        with path.joinpath(file_name).open(mode=mode) as file:
            LOGGER.debug("<%s.%s> | Wrote data to file %s located at: %s", __name__, "write_data_to_file", path, file_name)
            if isinstance(data, bytes):
                file.write(data.decode(encoding="utf-8"))
            elif isinstance(data, dict):
                file.write(json.dumps(data, **kwargs))
            elif isinstance(data, list):
                if isinstance(data[0], dict):
                    file.write(json.dumps(data, **kwargs))
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

    def type_builder(self, data: dict, new_list: list) -> list[str]:
        for key, value in data.items():
            # print(key, type(value), value)
            if isinstance(value, dict):
                new_list.append(self.type_builder(value, new_list))
                continue
            new_list.append(f"{key}: {type(value)}")
        return new_list


# TODO: Add a function to get a table's schema (with or without data)
class SQLHandler:
    """Generic ASQlite handler.

    Supports:
    - Creating Tables
    - Adding | Removing Columns
    - Adding | Removing Constraints
    - Renaming Columns and Tables.

    """

    _pool: Optional[asqlite.Pool]

    @property
    def pool(self) -> Optional[asqlite.Pool]:
        """ASQLITE Database connection pool."""
        return self._pool

    async def add_column(self, table: str, column: str, constraints: Iterable[str]) -> None:
        """Add a column to an existing table.

        Parameters
        ----------
        table: :class:`str`
            The name of the table to alter.
        column: :class:`str`
            The name of the new column.
        constraints: :class:`Iterable[str]`
            The column type and any constraints, e.g. ``["TEXT", "NOT NULL", "DEFAULT ''"]``.

        """
        column_def = " ".join(constraints)
        sql = f"ALTER TABLE {table} ADD COLUMN {column} {column_def}"
        if self.pool is None:
            LOGGER.error("<%s.add_column> | Our connection pool is `None`.", __class__.__name__)
            return
        async with self.pool.acquire() as conn:
            await conn.execute(sql)
            await conn.commit()
        LOGGER.info("<%s.add_column> | Added column '%s' to table '%s'.", __class__.__name__, column, table)

    async def add_constraints(self, table: str, column: str, constraints: Iterable[str]) -> None:
        """Add constraints to an existing column.

        This function does not catch any errors, such as duplicate constraints/etc.

        Parameters
        ----------
        table: :class:`str`
            The name of the table to alter.
        column: :class:`str`
            The name of the existing column to add constraints to.
        constraints: :class:`Iterable[str]`
            The constraints to add, e.g. ``["NOT NULL", "DEFAULT ''"]``.

        """
        column_def = " ".join(constraints)
        sql = f"ALTER TABLE {table} ADD CONSTRAINT {column} {column_def}"
        if self.pool is None:
            LOGGER.error("<%s.add_constraints> | Our connection pool is `None`.", __class__.__name__)
            return
        async with self.pool.acquire() as conn:
            await conn.execute(sql)
            await conn.commit()
        LOGGER.debug(
            "<%s.add_constraints> | Added constraints to column '%s' in table '%s' | Constraints: %s.",
            __class__.__name__,
            column,
            table,
            column_def,
        )

    async def change_column_name(self, table: str, column: str, new_column: str) -> None:
        """Rename a column on an existing table.

        Parameters
        ----------
        table: :class:`str`
            The name of the table to alter.
        column: :class:`str`
            The current name of the column.
        new_column: :class:`str`
            The new name for the column.

        """
        sql = f"ALTER TABLE {table} RENAME COLUMN {column} TO {new_column}"
        if self.pool is None:
            LOGGER.error("<%s.change_column_name> | Our connection pool is `None`.", __class__.__name__)
            return
        async with self.pool.acquire() as conn:
            await conn.execute(sql)
            await conn.commit()
        LOGGER.debug("<%s.change_column_name> | Renamed column '%s' to '%s' on table '%s'.", __class__.__name__, column, new_column, table)

    async def create_pool(
        self,
        database: Union[str, bytes],
        *,
        init: Optional[Callable[[sqlite3.Connection], None]] = None,
        size: int = 10,
        **kwargs: Any,
    ) -> Optional[asqlite.Pool]:
        """Generic wrapper for handling the :class:`asqlite` library ``create_pool`` function.

        Parameters
        ----------
        database: :class:`Union[str, bytes]`
            The path to the SQLite database file.
        init: :class:`Optional[Callable[[sqlite3.Connection], None]]`, optional
            An optional callable to initialize the connection, by default ``None``.
        size: :class:`int`, optional
            The number of connections to keep in the pool, by default ``10``.
        **kwargs: :class:`Any`
            Any additional kwargs passed to :func:`asqlite.create_pool`.

        Returns
        -------
        :class:`Optional[asqlite.Pool]`
            The connection pool, or ``None`` if an error occurred.

        """
        try:
            self._pool = await asqlite.create_pool(database=database, init=init, size=size, **kwargs)  # pyright: ignore[reportAttributeAccessIssue] # We know it will resolve to an `asqlite.Pool` object.
        except Exception as e:
            LOGGER.exception("<%s.%s> | Encountered an error creating our pool", __class__.__name__, "create_pool", exc_info=e)
            self._pool = None
        return self._pool

    async def create_table(self, schema: str) -> None:
        """Create a table using the provided schema SQL.

        Parameters
        ----------
        schema: :class:`str`
            The full ``CREATE TABLE`` SQL statement to execute.

        """
        if self.pool is None:
            LOGGER.error("<%s.create_table> | Our connection pool is `None`.", __class__.__name__)
            return
        async with self.pool.acquire() as conn:
            await conn.execute(schema)
            await conn.commit()
        LOGGER.debug("<%s.create_table> | Created table using schema: %s", __class__.__name__, schema)

    async def drop_column(self, table: str, column: str) -> None:
        """Drop a column from an existing table.

        Parameters
        ----------
        table: :class:`str`
            The name of the table to alter.
        column: :class:`str`
            The name of the column to drop.

        """
        sql = f"ALTER TABLE {table} DROP COLUMN {column}"
        if self.pool is None:
            LOGGER.error("<%s.drop_column> | Our connection pool is `None`.", __class__.__name__)
            return
        async with self.pool.acquire() as conn:
            await conn.execute(sql)
            await conn.commit()
        LOGGER.debug("<%s.drop_column> | Dropped column '%s' from table '%s'.", __class__.__name__, column, table)

    async def drop_constraints(self, table: str, column: str, constraints: Iterable[str]) -> None:
        """Remove constraints from an existing column.

        This function does not catch any errors or validate constraints.

        Parameters
        ----------
        table: :class:`str`
            The name of the table to alter.
        column: :class:`str`
            The name of the existing column to remove constraints from.
        constraints: :class:`Iterable[str]`
            The constraints to remove, e.g. ``["NOT NULL", "DEFAULT ''"]``.

        """
        column_def = " ".join(constraints)
        sql = f"ALTER TABLE {table} DROP CONSTRAINT {column} {column_def}"
        if self.pool is None:
            LOGGER.error("<%s.drop_constraints> | Our connection pool is `None`.", __class__.__name__)
            return
        async with self.pool.acquire() as conn:
            await conn.execute(sql)
            await conn.commit()
        LOGGER.debug(
            "<%s.drop_constraints> | Dropped Constraints from '%s' to table '%s' | Constraints: %s.",
            __class__.__name__,
            column,
            table,
            column_def,
        )

    async def rename_table(self, table: str, new_table: str) -> None:
        """Rename an existing table.

        Parameters
        ----------
        table: :class:`str`
            The current name of the table.
        new_table: :class:`str`
            The new name for the table.

        """
        sql = f"ALTER TABLE {table} RENAME TO {new_table}"
        if self.pool is None:
            LOGGER.error("<%s.rename_table> | Our connection pool is `None`.", __class__.__name__)
            return
        async with self.pool.acquire() as conn:
            await conn.execute(sql)
            await conn.commit()
        LOGGER.debug("<%s.rename_table> | Renamed table '%s' to '%s'.", __class__.__name__, table, new_table)


class LogHandler:
    """Local Log Handler.

    Discord Multi-line code block formats:
    - https://github.com/highlightjs/highlight.js/blob/main/SUPPORTED_LANGUAGES.md

    """

    cur_log: Path
    code_formats: ClassVar[list[str]] = ["excel", "nc", "ml", " nim", " ps", " prolog", "thor"]
    default_code_format: str = "ps"

    def __init__(self, sentry: str = "", level: int = logging.INFO, webhook_url: str = "", local_dev: bool = True) -> None:  # noqa: D107
        if not local_dev:
            LOGGER.info("Sentry SDK is Enabled -- Flag: %s", local_dev)
            # sentry_sdk.init(dsn=sentry, integrations=[AioHttpIntegration(), AsyncioIntegration()])
        else:
            LOGGER.warning("Sentry SDK is Disabled -- Flag: %s", local_dev)
        # self.webhook_url: str = webhook_url
        # self.session: aiohttp.ClientSession
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
_parser.add_argument("-build", help="Run our build_test() function", default=False, required=False, action="store_true")
# uv sync -n --upgrade-package foo
_parser.add_argument("--upgrade", help="Run `uv sync -n --upgrade-package package_name`")
# If I want to add a group, this is what I use.
# group: argparse._MutuallyExclusiveGroup = _parser.add_mutually_exclusive_group(required=False)
_parser.add_argument("-info", help="Set the logging level to `INFO`.", default=False, required=False, action="store_true")
_parser.add_argument("-debug", help="Set the logging level to `INFO`.", default=False, required=False, action="store_true")
_parsed_args: Launcher = _parser.parse_known_args(namespace=Launcher())[0]

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
    subprocess.run(["uv", "sync", "-n", "--upgrade-package", _parsed_args.upgrade], check=False)  # noqa: S603
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
