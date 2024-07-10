from openciv.gameplay.improvement import Improvement
from openciv.gameplay.tile_yield import TileYield
from openciv.engine.managers.i18n import _t


class MissileSilo(Improvement):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.improvement.military.missile_silo",
            _t("content.improvements.core.military.missile_silo.name"),
            _t("content.improvements.core.military.missile_silo.description"),
            *args,
            **kwargs,
        )

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="missile_silo", food=1.0, mode=TileYield.ADDITIVE)
