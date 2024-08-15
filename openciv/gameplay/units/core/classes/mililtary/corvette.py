from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.mililtary._base import CoreMilitaryBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class CorvettePromotion(Promotion):
    pass


class CoastRaider(CorvettePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.coast_raider",
            name=t_("content.units.core.promotions.corvette.coast_raider.name"),
            description=t_("content.units.core.promotions.corvette.coast_raider.description"),
            *args,
            **kwargs,
        )


class SeaRaider(CorvettePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.sea_raider",
            name=t_("content.units.core.promotions.corvette.sea_raider.name"),
            description=t_("content.units.core.promotions.corvette.sea_raider.description"),
            *args,
            **kwargs,
        )


class Mines(CorvettePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.mines",
            name=t_("content.units.core.promotions.corvette.mines.name"),
            description=t_("content.units.core.promotions.corvette.mines.description"),
            *args,
            **kwargs,
        )


class EscortDuty(CorvettePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.escort_duty",
            name=t_("content.units.core.promotions.corvette.escort_duty.name"),
            description=t_("content.units.core.promotions.corvette.escort_duty.description"),
            *args,
            **kwargs,
        )


class AgileManoevring(CorvettePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.agile_manoeuvring",
            name=t_("content.units.core.promotions.corvette.agile_manoeuvring.name"),
            description=t_("content.units.core.promotions.corvette.agile_manoeuvring.description"),
            *args,
            **kwargs,
        )


class CommandoPromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.corvette", *args, **kwargs)

    def register_promotions(self):
        coast_raider = CoastRaider(promotion_tree=self)
        sea_raider = SeaRaider(promotion_tree=self)
        mines = Mines(promotion_tree=self)
        escort_duty = EscortDuty(promotion_tree=self)
        agile_manoevring = AgileManoevring(promotion_tree=self)

        coast_raider.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        sea_raider.requires = RequiresPromotionComplete(promotion=coast_raider)
        mines.requires = RequiresPromotionComplete(promotion=sea_raider)
        escort_duty.requires = RequiresPromotionComplete(promotion=mines)
        agile_manoevring.requires = RequiresPromotionComplete(promotion=escort_duty)

        self.add_promotion(promotion=coast_raider)
        self.add_promotion(promotion=sea_raider)
        self.add_promotion(promotion=mines)
        self.add_promotion(promotion=escort_duty)
        self.add_promotion(promotion=agile_manoevring)


class Corvete(CoreMilitaryBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.corvette",
            name=t_("content.units.classes.core.corvette.name"),
            description=t_("content.units.classes.core.corvette.description"),
            icon=None,
            *args,
            **kwargs,
        )
