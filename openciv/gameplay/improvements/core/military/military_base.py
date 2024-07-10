from openciv.gameplay.improvement import Improvement
from openciv.gameplay.tile_yield import TileYield
from openciv.engine.managers.i18n import _t


class MilitaryBase(Improvement):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.improvement.military.military_base",
            _t("content.improvements.core.military.military_base.name"),
            _t("content.improvements.core.military.military_base.description"),
            *args,
            **kwargs,
        )

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="military_base", food=1.0, mode=TileYield.ADDITIVE)
