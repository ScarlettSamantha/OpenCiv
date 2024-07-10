from openciv.gameplay.improvement import Improvement
from openciv.gameplay.tile_yield import TileYield
from openciv.engine.managers.i18n import _t


class Castle(Improvement):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.improvement.military.castle",
            _t("content.improvements.core.military.castle.name"),
            _t("content.improvements.core.military.castle.description"),
            *args,
            **kwargs,
        )

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="Castle", food=1.0, mode=TileYield.ADDITIVE)
