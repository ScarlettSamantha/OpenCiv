from openciv.gameplay.improvement import Improvement
from openciv.gameplay.tile_yield import TileYield
from openciv.engine.managers.i18n import _t


class HotWaterSprings(Improvement):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.improvement.general.hot_water_springs",
            _t("content.improvements.core.general.hot_water_springs.name"),
            _t("content.improvements.core.general.hot_water_springs.description"),
            *args,
            **kwargs,
        )

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="hot_water_springs", food=1.0, mode=TileYield.ADDITIVE)
