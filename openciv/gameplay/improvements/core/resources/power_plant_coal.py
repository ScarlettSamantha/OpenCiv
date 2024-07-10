from openciv.gameplay.improvement import Improvement
from openciv.gameplay.tile_yield import TileYield
from openciv.engine.managers.i18n import _t


class PowerPlantCoal(Improvement):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.improvement.resource.power_plant_coal",
            _t("content.improvements.core.resource.power_plant_coal.name"),
            _t("content.improvements.core.resource.power_plant_coal.description"),
            *args,
            **kwargs,
        )

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="power_plant_gas", food=1.0, mode=TileYield.ADDITIVE)
