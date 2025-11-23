"""Copyright (C) 2021-2025 Katelynn Cadwallader.

This file is part of Moogle's Intuition.

Moogle's Intuition is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3, or (at your option)
any later version.

Moogle's Intuition is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
License for more details.

You should have received a copy of the GNU General Public License
along with Moogle's Intuition; see the file COPYING.  If not, write to the Free
Software Foundation, 51 Franklin Street - Fifth Floor, Boston, MA
02110-1301, USA.
"""

from __future__ import annotations

from typing import Any, NotRequired, TypedDict, Union

DataTypeAliases = Union[list["PartialIndex"]]

# ! Note, Save the `Response` suffix for top level JSON structure(if possible).


class MultiPartResponse(TypedDict):
    """The JSON structure for multiple :class:`GarlandTools` functions.

    - Typically the `fetch all` type endpoints eg :class:`GarlandTools.achievements()`.
    """

    browse: DataTypeAliases


class AchievementResponse(TypedDict):
    """The JSON structure from :class:`GarlandToolsAsync.achievement()`."""

    achievement: Achievement


class Achievement(TypedDict):
    id: int
    name: str
    description: str
    patch: float
    points: int
    category: int
    icon: int


class Action(TypedDict):
    categoryIndex: dict[str, IDName]


class Coffer(TypedDict):
    items: list[int]


class Craft(TypedDict):
    id: int
    job: int
    rlvl: int
    durability: int
    quality: int
    progress: int
    lvl: int
    materialQualityFactor: int
    yield_: NotRequired[int]
    hq: int
    quickSynth: int
    complexity: NQHQ
    stars: NotRequired[int]
    craftsmanshipReq: NotRequired[int]
    quickSynthCraftsmanship: NotRequired[int]
    unlockId: NotRequired[int]
    ingredients: NotRequired[list[IDAmount | IDAmountQuality]]


class DataResponse(TypedDict):
    """The JSON structure from :class:`GarlandToolsAsync.data()`."""

    patch: PatchData
    xp: list[int]
    jobs: list[JobData]
    # The key `id` in JobCategories is the same key for the attribute key.
    jobCategories: dict[str, JobCategories]
    # The key `id` in Dyes is the same key for the attribute key.
    dyes: dict[str, IDName]
    # The key `id` for NodeBonusIndex is the same key for the attribute key.
    nodeBonusIndex: dict[str, NodeBonusIndex]
    # The key `id` in LocationIndex is the same key for the attribute key.
    locationIndex: dict[str, LocationIndex]
    skywatcher: Skywatcher
    questGenreIndex: dict[str, QuestGenreIndex]
    ventureIndex: dict[str, VentureIndex]
    action: Action
    achievementCategoryIndex: dict[str, IDNameKind]
    materiaJoinRates: MateriaJoinRates
    voyages: Voyages
    item: ItemData


class Equipment(TypedDict):
    slot: int
    model: str
    id: NotRequired[int]
    uncertainty: NotRequired[bool]

class GearResponse(TypedDict):
    """The JSON structure from :class:`GarlandToolsAsync.endgame_gear()` and :class:`GarlandToolsAsync.leveling_gear()`."""

    equip: dict[str, list[dict[str, int]]]
    partials: list[PartialTypeIDObj]


class FateResponse(TypedDict):
    """The JSON structure from :class:`GarlandToolsAsync.fate()`."""

    fate: Fate


class Fate(TypedDict):
    id: int
    name: str
    description: str
    patch: float
    lvl: int
    maxlvl: int
    type: str
    zoneid: int
    coords: list[int]
    items: list[int]


class Fights(TypedDict):
    type: str
    currency: list[IDAmount]
    coffer: Coffer


class Fish(TypedDict):
    guide: str
    "Appears to be a little guide or tip; just a duplicate of the `description`"
    icon: int
    "Appears to be the fishing Guide Icon ID."
    spots: list[FishingSpots]
    "This related to information stored on `https://en.ff14angler.com` website."


class FishingSpots(TypedDict):
    spot: int
    "Possibly related to a map/loc, same field as `fishingSpots` - `https://www.garlandtools.org/db/#fishing/{spot}`"
    hookset: str
    tug: str
    "The strength of the bite."
    ff14angerId: int
    "This key belongs to the FF14 Angler Website. - `https://{language}.ff14angler.com/fish/{ff14angerId}`"
    baits: list[list[int]]
    "This key has a list of ints that relate to garlandtools urls. -`https://www.garlandtools.org/db/#item/{baits.id}`"


class IDLvl(TypedDict):
    id: int
    lvl: int


class IDName(TypedDict):
    id: int
    name: str


class IDNameKind(IDName, TypedDict):
    kind: str


class IDNameAttr(IDName, TypedDict):
    attr: str


class IDNum(TypedDict):
    id: int
    num: int


class IDType(TypedDict):
    id: int
    type: int


class IDAmount(TypedDict):
    id: int
    amount: int


class IDAmountQuality(IDAmount, TypedDict):
    quality: float


class IDCount(TypedDict):
    id: int
    count: int


class Ingredients(TypedDict):
    name: str
    id: int
    icon: int
    category: int
    ilvl: int
    price: int
    reducedFrom: NotRequired[list[int]]
    voyages: NotRequired[list[IDType]]
    desynthedFrom: NotRequired[list[int]]
    treasure: list[int]
    tradeShops: NotRequired[list[TradeShops]]
    instances: NotRequired[list[int]]
    ventures: NotRequired[list[int]]
    drops: NotRequired[list[int]]
    nodes: list[int]
    seeds: NotRequired[list[int]]
    craft: NotRequired[list[Craft]]
    vendors: NotRequired[list[int]]


class InstanceResponse(TypedDict):
    """The JSON structure from :class:`GarlandToolsAsync.instance()`."""

    instance: InstanceData
    partials: PartialTypeIDObj


class InstanceData(TypedDict):
    name: str
    category: str
    description: str
    id: int
    patch: float
    categoryIcon: int
    time: int
    min_lvl: int
    fullIcon: int
    healer: int
    tank: int
    ranged: int
    melee: int
    max_lvl: int
    min_ilvl: int
    rewards: list[int]
    fights: list[Fights]
    unlockedByQuest: int


class Item(TypedDict):
    id: int
    name: str
    description: str
    jobCategories: NotRequired[str]
    repair: NotRequired[int]
    equip: NotRequired[int]
    sockets: NotRequired[int]
    glamourerous: NotRequired[int]
    "possibly use as a bool"
    elvl: NotRequired[int]
    jobs: NotRequired[int]
    patch: float
    patchCategory: int
    price: int
    ilvl: int
    category: int
    dyecount: int
    tradeable: bool
    sell_price: int
    rarity: int
    stackSize: int
    icon: int

    # Most Items may or may not have these values below.
    nodes: NotRequired[list[int]]
    vendors: NotRequired[list[int]]
    tradeShops: NotRequired[list[TradeShops]]
    ingredients_of: NotRequired[dict[str, int]]
    "The Crafted Item ID as the KEY and the VALUE is the number of them to make the Crafted Item."
    levels: NotRequired[list[int]]
    desyntheFrom: NotRequired[list[int]]
    desynthedTo: NotRequired[list[int]]
    alla: NotRequired[dict[str, list[str]]]

    supply: NotRequired[dict[str, int]]
    "The Grand Company Supply Mission. Keys: count: int, xp: int, seals: int"
    drops: NotRequired[list[int]]
    craft: NotRequired[list[Craft]]
    ventures: NotRequired[list[int]]
    tradeCurrency: NotRequired[list[TradeShops]]

    # Weapons/Gear Keys
    attr: NotRequired[ItemAttribute]
    att_hq: NotRequired[ItemAttribute]
    attr_max: NotRequired[ItemAttribute]
    "The items(in terms of sequence) just below this in terms of ilvl/stats"
    downgrades: NotRequired[list[int]]
    models: NotRequired[list[str]]
    repair_item: NotRequired[int]
    "The Garland Tools Item ID to repair the Weapon/Gear"
    sharedModels: NotRequired[list[Any]]
    "??? Unsure what data struct this is."
    slot: NotRequired[int]
    "The Item slot on the Equipment panel"
    upgrades: NotRequired[list[int]]  #
    "The items(in terms of sequence) just above this in terms of ilvl/stats"

    # This belows to Fish type items specifically.
    fish: NotRequired[Fish]
    fishingSpots: NotRequired[list[int]]
    "This probably belongs to FFXIV and lines up with a Zone ID"


class ItemAttribute(TypedDict):
    pysical_damage: int
    magic_damage: int
    delay: float
    strength: int
    dexterity: int
    vitality: int
    intelligence: int
    mind: int
    piety: int
    gp: int
    cp: int
    tenacity: int
    direct_hit_rate: int
    critical_hit: int
    fire_resistance: int
    ice_resistance: int
    wind_resistance: int
    earth_resistance: int
    lightning_resistance: int
    water_resistance: int
    determination: int
    skill_speed: int
    spell_speed: int
    slow_resistance: int
    petrification_resistance: int
    paralysis_resistance: int
    silence_resistance: int
    blind_resistance: int
    poison_resistance: int
    stun_resistance: int
    sleep_resistance: int
    bind_resistance: int
    heavy_resistance: int
    doom_resistance: int
    craftsmanship: int
    control: int
    gathering: int
    perception: int


class ItemData(TypedDict):
    categoryIndex: dict[str, IDNameAttr]
    specialBonusIndex: dict[str, IDName]
    seriesIndex: dict[str, IDName]
    partialIndex: dict[str, PartialIndex]
    ingredients: dict[str, Ingredients]


class ItemRateAMount(TypedDict):
    item: int
    rate: float
    amount: int


class ItemResponse(TypedDict):
    """The JSON structure from :class:`GarlandTools.item()` function."""

    item: Item
    ingredients: NotRequired[list[Ingredients]]
    partials: NotRequired[list[PartialTypeIDObj]]


class JobCategories(TypedDict):
    id: int
    name: str
    jobs: list[int]


class JobData(TypedDict):
    id: int
    abbreviation: str
    category: str
    name: str
    startingLevel: int
    isJob: NotRequired[int]


class LocationIndex(TypedDict):
    id: int
    name: str
    parentId: NotRequired[int]
    size: NotRequired[float]
    weatherRate: NotRequired[int]


class LeveResponse(TypedDict):
    """The JSON structure from :class:`GarlandTools.leve()` function."""

    leve: Leve
    rewards: Rewards
    ingredients: list[Ingredients]
    partials: list[PartialTypeIDObj]


class Leve(TypedDict):
    id: int
    name: str
    descrption: str
    patch: float
    client: str
    lvl: int
    jobCategory: int
    levemete: int
    areaid: int
    xp: int
    gil: int
    rewards: int
    plate: int
    frame: int
    areaicon: int
    requires: list[dict[str, int]]
    complexity: NQHQ


class Rewards(TypedDict):
    id: int
    entries: list[ItemRateAMount]


class Materia(TypedDict):
    tier: int
    value: int
    attr: str
    category: int
    advancedMeldingForbidden: NotRequired[bool]


class MateriaJoinRates(TypedDict):
    nq: list[int]
    hq: list[int]


class MobResponse(TypedDict):
    """The JSON structure from :class:`GarlandTools.mob()` function."""

    mob: Mob


class Mob(TypedDict):
    id: int
    name: str
    quest: int
    zoneid: int
    lvl: str


class Name(TypedDict):
    name: str


class NodeBonusIndex(TypedDict):
    id: int
    condition: str
    bonus: str


class NodeResponse(TypedDict):
    """The JSON structure from :class:`GarlandTools.node()` function."""

    node: Node
    partials: list[PartialTypeIDObj]


class Node(TypedDict):
    id: int
    name: str
    patch: float
    type: int
    lvl: int
    points: list[IDCount]
    items: list[dict[str, int]]
    bonus: list[int]
    zoneid: int
    areaid: int
    radius: int
    coords: list[float]


class NPC(TypedDict):
    name: str
    id: int
    patch: float
    title: NotRequired[str]
    coords: list[float | str]
    zoneid: int
    areaid: int
    appearance: NotRequired[NPCAppearance]
    photo: NotRequired[str]
    "eg. Enpc_1000236.png"
    alts: NotRequired[list[int]]
    appalts: NotRequired[list[int]]
    trade: NotRequired[bool]
    shops: NotRequired[list[Shop]]
    equipment: NotRequired[list[Equipment]]


class NPCAppearance(TypedDict):
    gender: str
    race: str
    tribe: str
    height: int
    face: int
    jaw: int
    eyebrows: int
    nose: int
    "Two numeric values separated by a comma. eg `24, 2`"
    skinColor: str
    "Typically a hex code. `#DAB29E`"
    skinColorCode: str
    bust: int
    hairStyle: int
    "Two numeric values separated by a comma. eg `1, 3`"
    hairColor: str
    "Typically a hex code. `#BFBFBF`"
    hairColorCode: str
    eyeSize: str
    eyeShape: int
    "Two numeric values separated by a comma. eg`2, 5`"
    eyeColor: str
    "Typically a hex code. `#B9AF90`"
    eyeColorCode: str
    mouth: int
    extraFeatureName: str
    extraFeatureShape: int
    extraFeatureSize: int
    hash: int  # 1864024670


class NPCResponse(TypedDict):
    """The JSON structure from :class:`GarlandAPIWrapper.npc()` function."""

    npc: NPC
    partials: list[PartialTypeIDObj]

class NQHQ(TypedDict):
    nq: int
    hq: int


class PatchData(TypedDict):
    current: str
    partialIndex: dict[str, Patch]
    categoryIndex: dict[str, str]


class Patch(TypedDict):
    id: str
    name: str
    series: str


class PartialIndex(TypedDict):
    i: int
    n: str
    b: NotRequired[str]
    c: NotRequired[int | list[int] | list[str]]
    f: NotRequired[int]
    g: NotRequired[int]
    j: NotRequired[int | None]
    l: NotRequired[str | int]  # noqa: E741
    p: NotRequired[int]
    q: NotRequired[int]
    r: NotRequired[int]
    s: NotRequired[int]
    t: NotRequired[str | int]
    x: NotRequired[float]
    y: NotRequired[float]
    z: NotRequired[int]
    materia: Materia
    min_level: NotRequired[int]
    max_level: NotRequired[int]
    min_ilvl: NotRequired[int]
    max_ilvl: NotRequired[int]


class PartialTypeIDObj(TypedDict):
    type: str
    id: str
    obj: PartialIndex


class QuestResponse(TypedDict):
    """The JSON structure from :class:`GarlandAPIWrapper.quest()` function."""

    quest: Quest
    partials: list[PartialTypeIDObj]


class Quest(TypedDict):
    name: str
    location: str
    id: int
    patch: float
    sort: int
    icon: int
    unlocksFunction: int
    eventIcon: int
    issuer: int
    target: int
    genre: int
    reward: Reward
    reqs: Reqs
    next: list[int]


class QuestGenreIndex(TypedDict):
    id: int
    name: str
    category: str
    section: str


class Reward(TypedDict):
    items: list[IDNum]


class Reqs(TypedDict):
    jobs: list[IDLvl]
    quests: list[int]


class SearchResponse(TypedDict):
    """The JSON structure from :class:`GarlandAPIWrapper.search()` function."""

    type: str
    "The type of the data. (eg. 'item', 'action', 'status', etc...)"
    id: str
    obj: PartialIndex

class Shop(TypedDict):
    name: str
    entries: list[ShopListings]
    trade: bool


class ShopListings(TypedDict):
    item: list[IDAmount]
    currency: list[IDAmount]


class StatusResponse(TypedDict):
    """The JSON structure from :class:`GarlandAPIWrapper.status()` function."""

    status: Status


class Status(TypedDict):
    name: str
    description: str
    id: int
    icon: int
    patch: float
    category: int
    canDispel: bool


class Skywatcher(TypedDict):
    weatherIndex: list[str]
    weatherRateIndex: dict[str, WeatherRateIndex]


class Submarine(TypedDict):
    name: str
    sea: str
    stars: int
    rank: int
    tanks: int


class TradeShops(TypedDict):
    shop: str
    "The Shop Name."
    npcs: list[int]
    "A list of NPC IDs."
    listings: list[ShopListings]


class VentureIndex(TypedDict):
    id: int
    jobs: int
    lvl: int
    cost: int
    minutes: int
    ilvl: NotRequired[list[int]]
    amount: NotRequired[list[int]]
    gathering: NotRequired[list[int]]
    name: NotRequired[str]
    random: NotRequired[int]


class Voyages(TypedDict):
    airship: dict[str, Name]
    submarine: dict[str, Submarine]


class WeatherRateIndex(TypedDict):
    id: int
    rates: list[WeatherRate]


class WeatherRate(TypedDict):
    weather: int
    rate: int
