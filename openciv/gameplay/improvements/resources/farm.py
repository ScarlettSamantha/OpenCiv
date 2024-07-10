from openciv.gameplay import Improvement, TileYield
from openciv.engine.managers.tags import Tags
from openciv.engine.managers.i18n import _t


class Farm(Improvement):
    def __init__(self):
        self.name = _t("content.improvements.core.farm.name")
        self.description_str = _t("content.improvements.core.farm.description")

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="Basic Farm", food=1.0, mode=TileYield.ADDITIVE)

        self.tags = Tags.add(["food", "tier_1", "tile", "builder"])
