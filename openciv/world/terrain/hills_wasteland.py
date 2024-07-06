from ._base_terrain import BaseTerrain

from ursina import Texture
from openciv.world.terrain.traits.land import hilly, buildable

class HillsWasteland(BaseTerrain):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = 'world.terrain.hills_wasteland'

        self.movement_modifier = 0.5
        self.water_availability = 0.25

        self._model = 'openciv/assets/models/tiles/hills_wasteland.obj'
        self._texture = Texture('openciv/assets/models/tiles/hills_wasteland.png')

        self.add_modifiers(hilly + buildable)
