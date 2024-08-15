from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.civilian._base import CoreCivilianBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class EngineerPromotion(Promotion):
    pass


class Fortifications(EngineerPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.fortifications",
            name=t_("content.units.core.promotions.engineer.fortifications.name"),
            description=t_("content.units.core.promotions.engineer.fortifications.description"),
            *args,
            **kwargs,
        )


class Repair(EngineerPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.repair",
            name=t_("content.units.core.promotions.engineer.repair.name"),
            description=t_("content.units.core.promotions.engineer.repair.description"),
            *args,
            **kwargs,
        )


class BridgeBuilding(EngineerPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.bridge_building",
            name=t_("content.units.core.promotions.engineer.bridge_building.name"),
            description=t_("content.units.core.promotions.engineer.bridge_building.description"),
            *args,
            **kwargs,
        )


class PowerLines(EngineerPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.power_lines",
            name=t_("content.units.core.promotions.engineer.power_lines.name"),
            description=t_("content.units.core.promotions.engineer.power_lines.description"),
            *args,
            **kwargs,
        )


class RenewableEnergy(EngineerPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.renewable_energy",
            name=t_("content.units.core.promotions.engineer.renewable_energy.name"),
            description=t_("content.units.core.promotions.engineer.renewable_energy.description"),
            *args,
            **kwargs,
        )


class CivilEngineering(EngineerPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.civil_engineering",
            name=t_("content.units.core.promotions.engineer.civil_engineering.name"),
            description=t_("content.units.core.promotions.engineer.civil_engineering.description"),
            *args,
            **kwargs,
        )


class EngineerPromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.engineer", *args, **kwargs)

    def register_promotions(self):
        fortifications = Fortifications()
        repair = Repair()
        bridge_building = BridgeBuilding()
        power_lines = PowerLines()
        renewable_energy = RenewableEnergy()
        civil_engineering = CivilEngineering()

        fortifications.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        repair.requires = RequiresPromotionComplete(promotion=fortifications)
        bridge_building.requires = RequiresPromotionComplete(promotion=repair)
        power_lines.requires = RequiresPromotionComplete(promotion=bridge_building)
        renewable_energy.requires = RequiresPromotionComplete(promotion=power_lines)
        civil_engineering.requires = RequiresPromotionComplete(promotion=renewable_energy)

        self.add_promotion(fortifications)
        self.add_promotion(repair)
        self.add_promotion(bridge_building)
        self.add_promotion(power_lines)
        self.add_promotion(renewable_energy)
        self.add_promotion(civil_engineering)


class Engineer(CoreCivilianBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.engineer",
            name=t_("content.units.classes.core.engineer.name"),
            description=t_("content.units.classes.core.engineer.description"),
            icon=None,
            *args,
            **kwargs,
        )
