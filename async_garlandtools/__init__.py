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

__title__ = "GarlandToolsAPI_wrapper"
__author__ = "k8thekat"
__license__ = "GNU"
__version__ = "1.5.0"
__credits__ = "Universalis, GarlandTools, GarlandTools-PIP and SquareEnix"

from typing import TYPE_CHECKING, Literal, NamedTuple

from ._enums import *
from .modules import *

if TYPE_CHECKING:
    from ._types import *


class VersionInfo(NamedTuple):  # noqa: D101
    major: int
    minor: int
    revision: int
    release_level: Literal["release", "development"]


version_info: VersionInfo = VersionInfo(  # noqa: F821
    major=1,
    minor=5,
    revision=1,
    release_level="release",
)

del VersionInfo
