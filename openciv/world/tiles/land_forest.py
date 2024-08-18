from __future__ import annotations
from openciv.world.tiles._base_tile import BaseTile
from openciv.world.terrain.flat_forest import FlatForest


class LandForest(BaseTile):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setTerrain(FlatForest)
