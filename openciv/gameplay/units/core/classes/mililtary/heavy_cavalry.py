from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.mililtary._base import CoreMilitaryBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class HeavyCavalryPromotion(Promotion):
    pass


class HeavyRaiders(HeavyCavalryPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.heavy_raiders",
            name=t_("content.units.core.promotions.heavy_cavalry.heavy_raiders.name"),
            description=t_("content.units.core.promotions.heavy_cavalry.heavy_raiders.description"),
            *args,
            **kwargs,
        )


class Armored(HeavyCavalryPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.armored",
            name=t_("content.units.core.promotions.heavy_cavalry.armored.name"),
            description=t_("content.units.core.promotions.heavy_cavalry.armored.description"),
            *args,
            **kwargs,
        )


class DefensiveTactics(HeavyCavalryPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.defensive_tactics",
            name=t_("content.units.core.promotions.heavy_cavalry.defensive_tactics.name"),
            description=t_("content.units.core.promotions.heavy_cavalry.defensive_tactics.description"),
            *args,
            **kwargs,
        )


class ShieldWall(HeavyCavalryPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.shield_wall",
            name=t_("content.units.core.promotions.heavy_cavalry.shield_wall.name"),
            description=t_("content.units.core.promotions.heavy_cavalry.shield_wall.description"),
            *args,
            **kwargs,
        )


class MountedArchers(HeavyCavalryPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.mounted_archery",
            name=t_("content.units.core.promotions.heavy_cavalry.mounted_archery.name"),
            description=t_("content.units.core.promotions.heavy_cavalry.mounted_archery.description"),
            *args,
            **kwargs,
        )


class Warhorses(HeavyCavalryPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.war_horses",
            name=t_("content.units.core.promotions.heavy_cavalry.war_horses.name"),
            description=t_("content.units.core.promotions.heavy_cavalry.war_horses.description"),
            *args,
            **kwargs,
        )


class HeavyCavalryPromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.heavy_cavalry", *args, **kwargs)

    def register_promotions(self):
        heavy_raiders = HeavyRaiders()
        armored = Armored()
        defensive_tactics = DefensiveTactics()
        shield_wall = ShieldWall()
        mounted_archers = MountedArchers()
        war_horses = Warhorses()

        heavy_raiders.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        armored.requires = RequiresPromotionComplete(promotion=heavy_raiders)
        defensive_tactics.requires = RequiresPromotionComplete(promotion=armored)
        shield_wall.requires = RequiresPromotionComplete(promotion=defensive_tactics)
        mounted_archers.requires = RequiresPromotionComplete(promotion=shield_wall)
        war_horses.requires = RequiresPromotionComplete(promotion=mounted_archers)

        self.add_promotion(promotion=heavy_raiders)
        self.add_promotion(promotion=armored)
        self.add_promotion(promotion=defensive_tactics)
        self.add_promotion(promotion=shield_wall)
        self.add_promotion(promotion=mounted_archers)


class HeavyCavalry(CoreMilitaryBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.heavy_cavalry",
            name=t_("content.units.classes.core.heavy_cavalry.name"),
            description=t_("content.units.classes.core.heavy_cavalry.description"),
            icon=None,
            *args,
            **kwargs,
        )
