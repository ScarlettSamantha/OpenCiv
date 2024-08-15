from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.mililtary._base import CoreMilitaryBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class CombatEngineerPromotion(Promotion):
    pass


class Fortifications(CombatEngineerPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.fortifications",
            name=t_("content.units.core.promotions.combat_engineer.fortifications.name"),
            description=t_("content.units.core.promotions.combat_engineer.fortifications.description"),
            *args,
            **kwargs,
        )


class Repair(CombatEngineerPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.repair",
            name=t_("content.units.core.promotions.combat_engineer.repair.name"),
            description=t_("content.units.core.promotions.combat_engineer.repair.description"),
            *args,
            **kwargs,
        )


class Demolitions(CombatEngineerPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.demolitions",
            name=t_("content.units.core.promotions.combat_engineer.demolitions.name"),
            description=t_("content.units.core.promotions.combat_engineer.demolitions.description"),
            *args,
            **kwargs,
        )


class ConstructionSpeed(CombatEngineerPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.construction_speed",
            name=t_("content.units.core.promotions.combat_engineer.construction_speed.name"),
            description=t_("content.units.core.promotions.combat_engineer.construction_speed.description"),
            *args,
            **kwargs,
        )


class ActiveRadarJamming(CombatEngineerPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.bridge_building",
            name=t_("content.units.core.promotions.combat_engineer.bridge_building.name"),
            description=t_("content.units.core.promotions.combat_engineer.bridge_building.description"),
            *args,
            **kwargs,
        )


class Combat_engineerPromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.combat_engineer", *args, **kwargs)

    def register_promotions(self):
        fortifications = Fortifications()
        repair = Repair()
        demolitions = Demolitions()
        construction_speed = ConstructionSpeed()
        active_radar_jamming = ActiveRadarJamming()

        fortifications.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        repair.requires = RequiresPromotionComplete(promotion=fortifications)
        demolitions.requires = RequiresPromotionComplete(promotion=repair)
        construction_speed.requires = RequiresPromotionComplete(promotion=demolitions)
        active_radar_jamming.requires = RequiresPromotionComplete(promotion=construction_speed)

        self.add_promotion(promotion=fortifications)
        self.add_promotion(promotion=repair)
        self.add_promotion(promotion=demolitions)
        self.add_promotion(promotion=construction_speed)
        self.add_promotion(promotion=active_radar_jamming)


class Engineer(CoreMilitaryBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.engineer",
            name=t_("content.units.classes.core.combat_engineer.name"),
            description=t_("content.units.classes.core.combat_engineer.description"),
            icon=None,
            *args,
            **kwargs,
        )
