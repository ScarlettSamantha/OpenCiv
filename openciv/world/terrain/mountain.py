from ._base_terrain import BaseTerrain
from ._base_terrain import rgb

from ursina import Texture

from openciv.world.terrain.traits.land import mountain

class Mountain(BaseTerrain):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = 'world.terrain.mountain'
        self.fallback_color = rgb(238, 255, 0)

        self.movement_modifier = 3
        self.water_availability = 0

        self._model = 'openciv/assets/models/tiles/mountain.obj'
        self._texture = Texture('openciv/assets/models/tiles/mountain.png')

        self.add_modifiers(mountain)
