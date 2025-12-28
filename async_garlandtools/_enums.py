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

from enum import Enum

__all__ = ["IconType", "Job", "Language"]


class Job(Enum):
    """Jobs Enum."""

    # Tanks
    PALADIN = "PLD"
    WARRIOR = "WAR"
    DARK_KNIGHT = "DRK"
    GUN_BREAKER = "GNB"
    # Healer
    WHITE_MAGE = "WHM"
    SCHOLAR = "SCH"
    ASTROLOGIAN = "AST"
    SAGE = "SGE"
    # Melee DPS
    MONK = "MNK"
    DRAGOON = "DRG"
    NINJA = "NIN"
    SAMURAI = "SAM"
    REAPER = "RPR"
    # Physical Ranged DPS
    BARD = "BRD"
    MACHINIST = "MCH"
    DANCER = "DNC"
    # Magical Ranged DPS
    BLACK_MAGE = "BLM"
    SUMMONER = "SMN"
    RED_MAGE = "RDM"
    BLUE_MAGE = "BLU"
    # Domain of the Hand
    CARPENTER = "CRP"
    BLACKSMITH = "BSM"
    ARMORER = "ARM"
    GOLDSMITH = "GSM"
    LEATHERWORKER = "LTW"
    WEAVER = "WVR"
    ALCHEMIST = "ALC"
    CULINARIAN = "CUL"
    # Domain of the Land
    MINER = "MIN"
    BOTANIST = "BTN"
    FISHER = "FSH"


class IconType(Enum):
    item = "item"
    achievement = "achievement"
    instance = "instance"
    job = "job"
    status = "status"
    action = "action"
    event = "event"
    mob = "mob"
    marker = "marker"
    node = "node"
    fate = "fate"
    item_custom = "item/custom"


class Language(Enum):
    English = "en"
    French = "fr"
    Dutch = "de"
    Japanese = "ja"
