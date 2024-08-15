from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.mililtary._base import CoreMilitaryBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class LightCavalryPromotion(Promotion):
    pass


class Skirmisher(LightCavalryPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.skirmisher",
            name=t_("content.units.core.promotions.light_cavalry.skirmisher.name"),
            description=t_("content.units.core.promotions.light_cavalry.skirmisher.description"),
            *args,
            **kwargs,
        )


class Scout(LightCavalryPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.scout",
            name=t_("content.units.core.promotions.light_cavalry.scout.name"),
            description=t_("content.units.core.promotions.light_cavalry.scout.description"),
            *args,
            **kwargs,
        )


class Flanking(LightCavalryPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.flanking",
            name=t_("content.units.core.promotions.light_cavalry.flanking.name"),
            description=t_("content.units.core.promotions.light_cavalry.flanking.description"),
            *args,
            **kwargs,
        )


class Harassment(LightCavalryPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.harassment",
            name=t_("content.units.core.promotions.light_cavalry.harassment.name"),
            description=t_("content.units.core.promotions.light_cavalry.harassment.description"),
            *args,
            **kwargs,
        )


class MountedArcher(LightCavalryPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.mounted_archer",
            name=t_("content.units.core.promotions.light_cavalry.mounted_archer.name"),
            description=t_("content.units.core.promotions.light_cavalry.mounted_archer.description"),
            *args,
            **kwargs,
        )


class Mobility(LightCavalryPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.mobility",
            name=t_("content.units.core.promotions.light_cavalry.mobility.name"),
            description=t_("content.units.core.promotions.light_cavalry.mobility.description"),
            *args,
            **kwargs,
        )


class LightCavalryPromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.light_cavalry", *args, **kwargs)

    def register_promotions(self):
        skirmisher = Skirmisher()
        scout = Scout()
        flanking = Flanking()
        harassment = Harassment()
        mounted_archer = MountedArcher()
        mobility = Mobility()

        skirmisher.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        scout.requires = RequiresPromotionComplete(promotion=skirmisher)
        flanking.requires = RequiresPromotionComplete(promotion=scout)
        harassment.requires = RequiresPromotionComplete(promotion=flanking)
        mounted_archer.requires = RequiresPromotionComplete(promotion=harassment)
        mobility.requires = RequiresPromotionComplete(promotion=mounted_archer)

        self.add_promotion(skirmisher)
        self.add_promotion(scout)
        self.add_promotion(flanking)
        self.add_promotion(harassment)
        self.add_promotion(mounted_archer)
        self.add_promotion(mobility)


class LightCavalry(CoreMilitaryBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.light_cavalry",
            name=t_("content.units.classes.core.light_cavalry.name"),
            description=t_("content.units.classes.core.light_cavalry.description"),
            icon=None,
            *args,
            **kwargs,
        )
