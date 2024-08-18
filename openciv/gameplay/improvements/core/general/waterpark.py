from __future__ import annotations
from openciv.gameplay.improvement import Improvement
from openciv.gameplay.tile_yield import TileYield
from openciv.engine.managers.i18n import _t


class Waterpark(Improvement):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.improvement.general.waterpark",
            _t("content.improvements.core.general.waterpark.name"),
            _t("content.improvements.core.general.waterpark.description"),
            *args,
            **kwargs,
        )

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="waterpark", food=1.0, mode=TileYield.ADDITIVE)
