from openciv.world.tiles._base_tile import BaseTile
from openciv.world.terrain.coast import Coast as CoastTerrain


class Coast(BaseTile):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setTerrain(CoastTerrain)
