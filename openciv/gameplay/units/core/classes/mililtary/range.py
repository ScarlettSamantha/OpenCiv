from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.mililtary._base import CoreMilitaryBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class RangePromotion(Promotion):
    pass


class Sharpshooter(RangePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.sharpshooter",
            name=t_("content.units.core.promotions.range.sharpshooter.name"),
            description=t_("content.units.core.promotions.range.sharpshooter.description"),
            *args,
            **kwargs,
        )


class VolleyFire(RangePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.volley_fire",
            name=t_("content.units.core.promotions.range.volley_fire.name"),
            description=t_("content.units.core.promotions.range.volley_fire.description"),
            *args,
            **kwargs,
        )


class RapidReload(RangePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.rapid_reload",
            name=t_("content.units.core.promotions.range.rapid_reload.name"),
            description=t_("content.units.core.promotions.range.rapid_reload.description"),
            *args,
            **kwargs,
        )


class Longbow(RangePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.longbow",
            name=t_("content.units.core.promotions.range.longbow.name"),
            description=t_("content.units.core.promotions.range.longbow.description"),
            *args,
            **kwargs,
        )


class FireArrows(RangePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.fire_arrows",
            name=t_("content.units.core.promotions.range.fire_arrows.name"),
            description=t_("content.units.core.promotions.range.fire_arrows.description"),
            *args,
            **kwargs,
        )


class Camouflage(RangePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.camouflage",
            name=t_("content.units.core.promotions.range.camouflage.name"),
            description=t_("content.units.core.promotions.range.camouflage.description"),
            *args,
            **kwargs,
        )


class RangePromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.range", *args, **kwargs)

    def register_promotions(self) -> None:
        sharpshooter = Sharpshooter()
        volley_fire = VolleyFire()
        rapid_reload = RapidReload()
        longbow = Longbow()
        fire_arrows = FireArrows()
        camouflage = Camouflage()

        sharpshooter.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        volley_fire.requires = RequiresPromotionComplete(promotion=sharpshooter)
        rapid_reload.requires = RequiresPromotionComplete(promotion=volley_fire)
        longbow.requires = RequiresPromotionComplete(promotion=rapid_reload)
        fire_arrows.requires = RequiresPromotionComplete(promotion=longbow)
        camouflage.requires = RequiresPromotionComplete(promotion=fire_arrows)

        self.add_promotion(promotion=sharpshooter)
        self.add_promotion(promotion=volley_fire)
        self.add_promotion(promotion=rapid_reload)
        self.add_promotion(promotion=longbow)
        self.add_promotion(promotion=fire_arrows)
        self.add_promotion(promotion=camouflage)


class Range(CoreMilitaryBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.range",
            name=t_("content.units.classes.core.range.name"),
            description=t_("content.units.classes.core.range.description"),
            icon=None,
            *args,
            **kwargs,
        )
