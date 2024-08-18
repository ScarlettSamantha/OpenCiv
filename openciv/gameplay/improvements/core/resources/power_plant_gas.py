from __future__ import annotations
from openciv.gameplay.improvement import Improvement
from openciv.gameplay.tile_yield import TileYield
from openciv.engine.managers.i18n import _t


class PowerPlantGas(Improvement):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.improvement.resource.power_plant_gas",
            _t("content.improvements.core.resource.power_plant_gas.name"),
            _t("content.improvements.core.resource.power_plant_gas.description"),
            *args,
            **kwargs,
        )

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="power_plant_gas", food=1.0, mode=TileYield.ADDITIVE)
