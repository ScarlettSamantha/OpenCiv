from ._base_terrain import BaseTerrain
from ._base_terrain import rgb

from ursina import Texture

from openciv.world.terrain.traits.water import open_water_lake

class lake(BaseTerrain):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = 'world.terrain.sea_water'
        self.fallback_color = rgb(0, 119, 255)
        self.movement_modifier = 0.5
        self._model = "openciv/assets/models/tiles/lake.obj"
        self._texture = Texture("openciv/assets/models/tiles/lake.png")

        self.add_modifiers(open_water_lake)
