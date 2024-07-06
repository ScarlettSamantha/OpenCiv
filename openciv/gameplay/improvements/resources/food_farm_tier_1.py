from openciv.gameplay import Improvement, TileYield
from openciv.engine.managers.tags import Tags


class Farm(Improvement):
    def __init__(self):
        self.name = "world.tiles.resource.food_farm_tier_1_name"
        self.description_str = "world.tiles.resource.food_farm_tier_1_description"

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="Basic Farm", food=1.0, mode=TileYield.ADDITIVE)

        self.tags = Tags.add(["food", "tier_1", "tile", "builder"])
