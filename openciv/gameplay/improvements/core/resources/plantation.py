from openciv.gameplay.improvement import Improvement
from openciv.gameplay.tile_yield import TileYield
from openciv.engine.managers.i18n import _t


class Plantation(Improvement):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.improvement.resource.plantation",
            _t("content.improvements.core.resource.plantation.name"),
            _t("content.improvements.core.resource.plantation.description"),
            *args,
            **kwargs,
        )

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="plantation", food=1.0, mode=TileYield.ADDITIVE)
