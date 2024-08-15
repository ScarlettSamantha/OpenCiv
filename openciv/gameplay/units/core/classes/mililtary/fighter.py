from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.mililtary._base import CoreMilitaryBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class FighterPromotion(Promotion):
    pass


class DogFighting(FighterPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.dogfighting",
            name=t_("content.units.core.promotions.fighter.dogfighting.name"),
            description=t_("content.units.core.promotions.fighter.dogfighting.description"),
            *args,
            **kwargs,
        )


class Flares(FighterPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.fighter_flares",
            name=t_("content.units.core.promotions.fighter.flares.name"),
            description=t_("content.units.core.promotions.fighter.flares.description"),
            *args,
            **kwargs,
        )


class Multirole(FighterPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.multirole",
            name=t_("content.units.core.promotions.fighter.multirole.name"),
            description=t_("content.units.core.promotions.fighter.multirole.description"),
            *args,
            **kwargs,
        )


class AirRepair(FighterPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.fighter_air_repair",
            name=t_("content.units.core.promotions.fighter.air_repair.name"),
            description=t_("content.units.core.promotions.fighter.air_repair.description"),
            *args,
            **kwargs,
        )


class NavyModifications(FighterPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.navy_modifications",
            name=t_("content.units.core.promotions.fighter.navy_modifications.name"),
            description=t_("content.units.core.promotions.fighter.navy_modifications.description"),
            *args,
            **kwargs,
        )


class FighterPromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.fighter", *args, **kwargs)

    def register_promotions(self):
        dogfighting = DogFighting()
        flares = Flares()
        multirole = Multirole()
        air_repair = AirRepair()
        navy_modifications = NavyModifications()

        dogfighting.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        flares.requires = RequiresPromotionComplete(promotion=dogfighting)
        multirole.requires = RequiresPromotionComplete(promotion=flares)
        air_repair.requires = RequiresPromotionComplete(promotion=multirole)
        navy_modifications.requires = RequiresPromotionComplete(promotion=air_repair)

        self.add_promotion(promotion=dogfighting)
        self.add_promotion(promotion=flares)
        self.add_promotion(promotion=multirole)
        self.add_promotion(promotion=air_repair)
        self.add_promotion(promotion=navy_modifications)


class Fighter(CoreMilitaryBaseClass):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.class.fighter",
            name=t_("content.units.classes.core.fighter.name"),
            description=t_("content.units.classes.core.fighter.description"),
            icon=None,
            *args,
            **kwargs,
        )
