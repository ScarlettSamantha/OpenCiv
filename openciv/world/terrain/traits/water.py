from __future__ import annotations
from openciv.gameplay.tile_modifiers import TileModifier
from openciv.world.terrain.traits.land import buildable

sailable = (TileModifier("sailable", True),)

coast = (TileModifier("deep", False),)
lake = (TileModifier("deep", False),)
sea = (TileModifier("deep", True),)

water = (TileModifier("walkable", False), TileModifier("climbable", False), TileModifier("flyable", True), TileModifier("space_above", True)) + sailable

open_water_coast = buildable + water + coast
open_water_lake = buildable + water + lake
open_water_sea = buildable + water + sea
