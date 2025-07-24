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
    browse: DataTypeAliases
    # achievement: NotRequired[Achievement]
    # fate: NotRequired[FateResponse]
    # mob: NotRequired[MobResponse]
    # npc: NotRequired[NPCResponse]
    # quest: NotRequired[QuestResponse]


class AchievementResponse(TypedDict):
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
    """The JSON structure from :class:`GarlandToolsAPI_ItemKeysTyped.craft`."""

    id: int  # 907
    job: int  # 15
    rlvl: int  # 4
    durability: int  # 40
    quality: int  # 104
    progress: int  # 10
    lvl: int  # 4
    materialQualityFactor: int  # 0
    yield_: NotRequired[int]  # 3
    hq: int  # 1
    quickSynth: int  # 1
    complexity: NQHQ  # {"nq": 31, "hq": 51}
    stars: NotRequired[int]
    craftsmanshipReq: NotRequired[int]
    quickSynthCraftsmanship: NotRequired[int]
    unlockId: NotRequired[int]
    ingredients: NotRequired[list[IDAmount | IDAmountQuality]]


class DataResponse(TypedDict):
    patch: PatchResponse
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


class GearResponse(TypedDict):
    equip: dict[str, list[dict[str, int]]]
    partials: list[PartialTypeIDObj]


class FateResponse(TypedDict):
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
    """The JSON structure from :class:`GarlandToolsAPI_CraftTyped.ingredients`."""

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
    fights: list[dict]
    unlockedByQuest: int


class Item(TypedDict):
    """The JSON structure for :class:`GarlandToolsAPI_ItemTyped.item`."""

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
    patch: int
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
    ingredients_of: NotRequired[
        dict[
            str,
            int,
        ]
    ]
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
    fish: NotRequired[ItemFish]
    fishingSpots: NotRequired[list[int]]
    "This probably belongs to FFXIV and lines up with a Zone ID"


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
    ingredients: list[Ingredients]
    partials: list[PartialTypeIDObj]


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
    leve: dict
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


class NQHQ(TypedDict):
    nq: int
    hq: int


class PatchResponse(TypedDict):
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
    type: Any
    id: str
    obj: PartialIndex


class StatusResponse(TypedDict):
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


# Old TypedDicts below..


class ItemAttribute(TypedDict):
    """The JSON structure for :class:`GarlandToolsAPI_ItemTyped.attr`."""

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


class ItemFish(TypedDict):
    """The JSON structure for :class:`GarlandToolsAPI_ItemTyped.fish`."""

    guide: str  # Appears to be a little Guide/tip; just a duplicate of the "description"
    icon: int  # Appears to be the fishing Guide ICON
    spots: list[ItemFishingSpots]


class ItemFishingSpots(TypedDict):
    """The JSON structure for :class:`GarlandToolsAPI_ItemFishTyped.spots`.

    Parameters
    ----------
    spot: :class:`int`
        Possibly related to a Map/loc -- Unsure.. Same field as `fishingSpots`.
        -> `https://www.garlandtools.org/db/#fishing/{spot}
    hookset: :class:`str`
        The type of Hook action to use
    tug: :class:`str`
        The strength of the bite
    ff14angerId: :class:`int`
        This key belongs to the FF14 Angler Website.
        - `https://{loc}.ff14angler.com/fish/{ff14angerId}`
    baits: :class:`list[list[int]]`
        This key has a list of ints that related to
        - `https://www.garlandtools.org/db/#item/{baits.id}`

    """

    spot: int
    hookset: str
    tug: str
    ff14angerId: int
    baits: list[list[int]]


class TradeShops(TypedDict):
    """The JSON structure from :class:`GarlandToolsAPI_Item.tradeShops`."""

    shop: str  # The Shop Name
    npcs: list[int]  # A list of NPC IDs.
    listings: list[ShopListings]


class ShopListings(TypedDict):
    """The JSON structure from :class:`GarlandToolsAPI_ItemTradeShopsTyped.listings`."""

    item: list[IDAmount]
    currency: list[IDAmount]


class NPCAppearance(TypedDict):
    """The JSON structure from :class:`GarlandToolsAPI_NPCTyped.appearance`."""

    gender: str  # "Female",
    race: str  # "Miqo'te",
    tribe: str  # "Seeker of the Sun",
    height: int  # 50,
    face: int  # 1,
    jaw: int  # 1,
    eyebrows: int  # 1,
    nose: int  # 1,
    skinColor: str  # "24, 2",
    skinColorCode: str  # "#DAB29E",
    bust: int  # 0,
    hairStyle: int  # 134201,
    hairColor: str  # "1, 3",
    hairColorCode: str  # "#BFBFBF",
    eyeSize: str  # "Large",
    eyeShape: int  # 1,
    eyeColor: str  # "2, 5",
    eyeColorCode: str  # "#B9AF90",
    mouth: int  # 1,
    extraFeatureName: str  # "Tail",
    extraFeatureShape: int  # 1,
    extraFeatureSize: int  # 50,
    hash: int  # 1864024670


class NPCResponse(TypedDict):
    npc: NPC


class NPC(TypedDict):
    """Tthe JSON structure from :class:`GarlandAPIWrapper.npc()` function."""

    name: str
    id: int
    patch: float
    title: NotRequired[str]
    coords: list[float | str]
    zoneid: int
    areaid: int
    appearance: NotRequired[NPCAppearance]
    photo: NotRequired[str]  # "Enpc_1000236.png"
