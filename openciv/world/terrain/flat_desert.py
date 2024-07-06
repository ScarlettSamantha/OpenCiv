from ._base_terrain import BaseTerrain

from ursina import Texture
from openciv.world.terrain.traits.land import buildable_flat_land


class FlatDesert(BaseTerrain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = "world.terrain.flatland_dessert"

        self.movement_modifier = 0.5
        self.water_availability = 0

        self._model = "openciv/assets/models/tiles/dessert2.obj"
        self._texture = Texture("openciv/assets/models/tiles/dessert2.png")

        self.add_modifiers(buildable_flat_land)
