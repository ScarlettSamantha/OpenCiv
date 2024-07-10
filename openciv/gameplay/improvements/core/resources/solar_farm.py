from openciv.gameplay.improvement import Improvement
from openciv.gameplay.tile_yield import TileYield
from openciv.engine.managers.i18n import _t


class SolarFarm(Improvement):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.improvement.resource.solar_farm",
            _t("content.improvements.core.resource.solar_farm.name"),
            _t("content.improvements.core.resource.solar_farm.description"),
            *args,
            **kwargs,
        )

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="solar_farm", food=1.0, mode=TileYield.ADDITIVE)
