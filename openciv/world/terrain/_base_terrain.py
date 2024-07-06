from ursina import rgb
from typing import List, Tuple

from openciv.gameplay.tile_modifiers import TileModifiers
from openciv.gameplay.tile_yield_modifier import TileYieldModifier


class BaseTerrain:
    def __init__(self):
        self.fallback_color = rgb(225, 0, 255)

        self.name = ""

        self.user_title = ""

        self._texture = ""
        self._model = "openciv/assets/models/tiles/base_testing.obj"

        self.movement_modifier = 0.0
        self.water_availability = 1.0
        self.radatiation = 0.0

        self.tile_modifiers: TileModifiers = TileModifiers()
        self.tile_yield_modifiers: TileYieldModifier = TileYieldModifier()

    def model(self):
        return self._model

    def texture(self):
        return self._texture

    def add_modifiers(self, modifiers: List["TileModifier"] | Tuple["TileModifier"]):  # noqa F821
        for item in modifiers:
            self.tile_modifiers.append(item)

    def add_tile_yield_modifier(self, tile_yield_modifier: TileYieldModifier):
        self.tile_yield_modifiers.append(tile_yield_modifier)

    def get_modifiers(self) -> TileModifiers:
        return self.tile_modifiers

    def color(self):
        return self.fallback_color
