from openciv.gameplay.improvement import Improvement
from openciv.gameplay.tile_yield import TileYield
from openciv.engine.managers.i18n import _t


class DesalinationPlant(Improvement):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.improvement.general.desalination_plant",
            _t("content.improvements.core.general.desalination_plant.name"),
            _t("content.improvements.core.general.desalination_plant.description"),
            *args,
            **kwargs,
        )

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="desalination_plant", food=1.0, mode=TileYield.ADDITIVE)
