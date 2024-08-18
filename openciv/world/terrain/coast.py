from __future__ import annotations
from ._base_terrain import BaseTerrain
from ._base_terrain import rgb

from ursina import Texture

from openciv.world.terrain.traits.water import open_water_coast

class Coast(BaseTerrain):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = 'world.terrain.coast'
        self.fallback_color = rgb(0, 119, 255)
        self.movement_modifier = 0.5
        self._model = "openciv/assets/models/tiles/water2.obj"
        self._texture = Texture("openciv/assets/models/tiles/water2.png")

        self.add_modifiers(open_water_coast)
