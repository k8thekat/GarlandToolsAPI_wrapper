class Snowflake:
    id: int

    _no_cache: str = "Attribute not cached, call <%s.garland_info_get> first. | Attribute: %s"
    no_market: str = "Attribute not cached, call <%s.set_current_marketboard> first. | Attribute: %s"


class Object(Snowflake):
    pass


class Item(Object):
    """Item _summary_.

    - Houses Garland Tools API Information.

    """

    # Cached attributes
    name: str
    description: str
    jobCategories: str
    repair: int
    equip: int
    sockets: int
    glamourerous: int  # possibly use as a bool
    elvl: int
    jobs: int
    id: int
    patch: GarlandToolsAPI_PatchEnum
    patchCategory: int
    price: int
    ilvl: int
    category: int
    dyecount: bool  # Converting the incoming int into a bool.
    tradeable: bool  # Converting the incoming int into a bool.
    sell_price: int
    rarity: int
    stackSize: int
    icon: int

    # These two keys come from the top level of the GarlandToolsAPI_ItemTyped.
    ingredients: list[GarlandToolsAPI_ItemIngredientsTyped]
    partials: list[GarlandToolsAPI_ItemPartialsTyped]

    # Most Items may or may not have these values below.
    nodes: list[int]
    vendors: list[int]
    tradeShops: list[GarlandToolsAPI_ItemTradeShopsTyped]
    ingredients_of: dict[str, int]  # The Crafted Item ID as the KEY and the VALUE is the number of them to make the Crafted Item.
    levels: list[int]
    desyntheFrom: list[int]
    desynthedTo: list[int]
    alla: dict[str, list[str]]
    supply: dict[str, int]  # The Grand Company Supply Mission. Keys: count: int, xp: int, seals: int
    drops: list[int]
    craft: list[GarlandToolsAPI_ItemCraftTyped]
    ventures: list[int]

    # Weapons/Gear Keys
    attr: GarlandToolsAPI_ItemAttrTyped
    att_hq: GarlandToolsAPI_ItemAttrTyped
    attr_max: GarlandToolsAPI_ItemAttrTyped
    downgrades: list[int]  # The items just below this in terms of ilvl/stats
    models: list[str]
    repair_item: int  # The Garland Tools Item ID to repair the Weapon/Gear
    sharedModels: list
    slot: int  # The Item slot on the Equipment panel
    upgrades: list[int]  # The items just above this in terms of ilvl/stats

    # This belows to Fish type items specifically.
    fish: GarlandToolsAPI_ItemFishTyped
    fishingSpots: list[int]  # This probably belongs to FFXIV and lines up with a Zone ID
    ff14anglerId: int  # This is the ID used to find the fish on FF14 Angler website.

    __base_slots__: tuple[str, ...] = (
        "item_id",
        "en_name",
        "de_name",
        "ja_name",
        "fr_name",
        "match_val",
        "__cached__",
        "_garland_api",
    )

    __cached__: bool
    __cached_slots__: tuple[str, ...] = (
        "name",
        "description",
        "jobCategories",
        "repair",
        "equip",
        "sockets",
        "glamourerous",
        "elvl",
        "jobs",
        "id",
        "patch",
        "patchCategory",
        "price",
        "ilvl",
        "category",
        "dyecount",
        "tradeable",
        "sell_price",
        "rarity",
        "stackSize",
        "icon",
        "nodes",
        "vendors",
        "tradeShops",
        "ingredients_of",
        "levels",
        "desyntheFrom",
        "desynthedTo",
        "alla",
        "supply",
        "drops",
        "craft",
        "ventures",
        "attr",
        "att_hq",
        "attr_max",
        "downgrades",
        "models",
        "repair_item",
        "sharedModels",
        "slot",
        "upgrades",
        "fish",
        "fishingSpots",
        "ff14anglerId",
        "ff14angler_url",
    )

    def get_garland_info(self) -> FFXIVItem:
        """Retrieves the GarlandTools API Item JSON info and updates our FFXIVItem object."""
        to_bool = ["tradeable", "glamourerous"]
        data: GarlandToolsAPI_ItemTyped = self._garland_api.item(item_id=int(self.item_id))
        item: GarlandToolsAPI_ItemKeysTyped | None = data.get("item", None)
        if item is None:
            self.logger.warning("Failed to find any information on Item ID: %s | Item Name: %s", self.item_id, self.en_name)
            return self
        self.ingredients = data.get("ingredients", [])
        self.partials = data.get("partials", [])
        for key, value in item.items():
            # print("GARLAND INFO TYPES", key, type(value), value)
            if key == "dyecount":
                if isinstance(value, int) and value > 0:
                    setattr(self, key, f"Yes, {value} slots.")
                else:
                    setattr(self, key, "No")

            elif key == "description":
                if isinstance(value, str) and len(value) > 0:
                    value = self.sanitize_html(data=value)
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)

            elif key == "patch":
                # print("FOUND PATCH", isinstance(value, int), value)
                if isinstance(value, float):
                    value = int(value)
                setattr(self, key, GarlandToolsAPI_PatchEnum(value=value))

            elif key in to_bool:
                if isinstance(value, int):
                    setattr(self, key, bool(value))
                else:
                    setattr(self, key, value)
            else:
                setattr(self, key, value)

            self.__cached__ = True
            self.ffxiv_wiki = f"https://ffxiv.consolegameswiki.com/wiki/{self.name.replace(' ', '_')}"
        return self

    # TODO - This may require knowing the item_type prior or setting an attribute of our self to properly resolve the Icon Type.
    def get_icon(self) -> discord.File:
        """Returns a :class:`discord.File` object with the filename set to "item-icon.png"."""
        res: discord.File | BytesIO = self._garland_api.icon(
            icon_type=GarlandToolsAPIIconTypeEnum.item, icon_id=int(self.icon), to_file=True
        )
        if isinstance(res, discord.File):
            return res
        return discord.File(fp=res, filename=f"{self.item_id}.png")

    def get_vendor_information(self) -> str | None:
        vendor_url = "https://www.garlandtools.org/db/#npc/"

        if self.__cached__ is False:
            raise AttributeError(self._no_cache)

        if self.vendors is None:
            return None

        temp: list[str] = []
        len_check: int = 0
        for npc in self.vendors:
            data: GarlandToolsAPI_NPCTyped = self._garland_api.npc(npc_id=npc)
            # Some of the cords are strings and not sure why, so we force to float.
            # Unsure if any data could be non numeric; so we try/except to be safe.
            try:
                cords: list = [float(i) for i in data.get("coords", [])]

            except ValueError:
                self.logger.warning(
                    "We encountered an Error converting NPC cords to Floats inside <gen_vendor_information>. | %s",
                    data.get("coords", []),
                )
                cords = data.get("coords", [])

            var: str = f"- **[{data.get('name', 'UNK')}]({vendor_url}/{data.get('id')})** | {cords}"
            len_check += len(var)
            if len_check > 1024:
                break

            temp.append(var)

        return "\n".join(sorted(temp))

    def get_craft_information(self) -> str | None:
        """Generates a str from the list of Craft Information regarding the Self(FFXIVItem) from Garland Tools API."""
        # JOB NAME | [INGREDIENT NAME (QTY)]
        if self.__cached__ is False:
            raise AttributeError(self._no_cache)

        if self.craft is None:
            return None

        temp: list[str] = []
        len_check: int = 0
        # print("CRAFTS", self.craft)
        for craftor in self.craft:
            ingredients: list[str] = []
            temp_ingredients: list[GarlandToolsAPI_ItemCraftIngredientsTyped] = craftor.get("ingredients", [])
            # print("TEMP INGREDIENTS", temp_ingredients)
            if len(temp_ingredients) == 0:
                continue

            for i in temp_ingredients:
                item: GarlandToolsAPI_ItemTyped = self._garland_api.item(item_id=i.get("id", 0))
                item_key: GarlandToolsAPI_ItemKeysTyped | None = item.get("item", None)
                if item_key is None:
                    continue
                ingredients.append(f"{i.get('amount')}x {item_key.get('name', 'N/A')}")

            t: str = ", ".join(ingredients)
            var: str = f"**{JobEnum(value=craftor.get('job', 0)).name.title()}**:\n `{t}`"
            len_check += len(var)
            if len_check > 1024:
                break
            # print("VAR", var)
            temp.append(var)

        return "\n".join(sorted(temp))

    def get_drops(self) -> str | None:
        mob_url = "https://www.garlandtools.org/db/#mob/"

        if self.__cached__ is False:
            raise AttributeError(self._no_cache)

        if self.drops is None:
            return None

        temp: list[str] = []
        len_check: int = 0
        for monster in self.drops:
            data: GarlandToolsAPI_MobTyped = self._garland_api.mob(mob_id=monster)

            var: str = f"Lv. {data['lvl']} | [{data['name']}]({mob_url + str(data['id'])}) | ZoneID: {data['zoneid']}"
            len_check += len(var)
            if len_check > 1024:
                break

            temp.append(var)
        return "\n".join(sorted(temp))

    def get_fish_guide(self) -> str | None:
        # Bait, hookset and tug does not change regardless of the spots location.

        if self.__cached__ is False:
            raise AttributeError(self._no_cache)

        if self.fish is None:
            return None
        self.ff14angler_url = f"https://en.ff14angler.com/fish/{self.ff14anglerId}"
        return self.fish.get("guide", "N/A")

    def get_fish_catching(self) -> Any:
        # it appears that the bait is tied to the location.
        # We can also have multiple spot's using different baits.
        # Each entry of "baits" starts off at Bait, Mooch, Mooch
        temp: list[str] = []

        spot_url = "https://wwww.garlandtools.org/db/#fishing/"  # ff14anglerId
        spots: list[GarlandToolsAPI_ItemFishSpotsTyped] = self.fish.get("spots", [])

        if len(spots) > 0:
            # This ID value is used to link to FF14Angler.com
            self.ff14anglerId = spots[0].get("ff14angerId", 0)

            temp.append(f"(discord_emoji) {spots[0].get('hookset', 'None')}")
            temp.append("-------")
            # TODO - Display [Location name](garland url) | [bait name](garland url) Bait | [bait name] Mooch | etc...
            for entry in spots:
                data: GarlandToolsAPI_FishingLocationsTyped | None = self._garland_api.fishing(spot_id=entry.get("spot", 0))
                if data is None:
                    continue
                temp.append(f"*{data.get('n')}")
                spot_bait: list[Any] = [self._garland_api.item(item_id=i) for i in spots[0].get("baits", [])]
                temp.append(f"{spots[0].get('baits', 'None')}")
            # Here we would generate a list of links with the [Fishing Spot Name](GarlandTools.org) | Location

    def get_partials(self) -> Any:
        pass

    def get_patch_icon(self) -> discord.File:
        """Takes the Patch ID from Garland Tools and converts it into a Enum to retrieve the proper Patch Icon for the item."""
        return discord.File(fp=FFXIVResource.resource_path.joinpath(f"{self.patch.name}-icon.png"), filename=f"{self.patch.name}.png")
