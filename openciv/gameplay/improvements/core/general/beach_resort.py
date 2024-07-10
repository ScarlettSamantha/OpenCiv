from openciv.gameplay.improvement import Improvement
from openciv.gameplay.tile_yield import TileYield
from openciv.engine.managers.i18n import _t


class BeachResort(Improvement):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.improvement.general.beach_resort",
            _t("content.improvements.core.general.beach_resort.name"),
            _t("content.improvements.core.general.beach_resort.description"),
            *args,
            **kwargs,
        )

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="beach_resort", food=1.0, mode=TileYield.ADDITIVE)
