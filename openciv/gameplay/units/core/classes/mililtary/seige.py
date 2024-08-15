from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.mililtary._base import CoreMilitaryBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class SeigePromotion(Promotion):
    pass


class BatteringRam(SeigePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.battering_ram",
            name=t_("content.units.core.promotions.seige.battering_ram.name"),
            description=t_("content.units.core.promotions.seige.battering_ram.description"),
            *args,
            **kwargs,
        )


class ArtilleryBarrage(SeigePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.artillery_barrage",
            name=t_("content.units.core.promotions.seige.artillery_barrage.name"),
            description=t_("content.units.core.promotions.seige.artillery_barrage.description"),
            *args,
            **kwargs,
        )


class SiegeTower(SeigePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.siege_tower",
            name=t_("content.units.core.promotions.seige.siege_tower.name"),
            description=t_("content.units.core.promotions.seige.siege_tower.description"),
            *args,
            **kwargs,
        )


class Catapult(SeigePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.catapult",
            name=t_("content.units.core.promotions.seige.catapult.name"),
            description=t_("content.units.core.promotions.seige.catapult.description"),
            *args,
            **kwargs,
        )


class EngineerSupport(SeigePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.engineer_support",
            name=t_("content.units.core.promotions.seige.engineer_support.name"),
            description=t_("content.units.core.promotions.seige.engineer_support.description"),
            *args,
            **kwargs,
        )


class DemolitionExpert(SeigePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.demolition_expert",
            name=t_("content.units.core.promotions.seige.demolition_expert.name"),
            description=t_("content.units.core.promotions.seige.demolition_expert.description"),
            *args,
            **kwargs,
        )


class SeigePromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.seige", *args, **kwargs)

    def register_promotions(self) -> None:
        battery_ram = BatteringRam()
        artillery_barrage = ArtilleryBarrage()
        siege_tower = SiegeTower()
        catapult = Catapult()
        engineer_support = EngineerSupport()
        demolition_expert = DemolitionExpert()

        battery_ram.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        artillery_barrage.requires = RequiresPromotionComplete(promotion=battery_ram)
        siege_tower.requires = RequiresPromotionComplete(promotion=artillery_barrage)
        catapult.requires = RequiresPromotionComplete(promotion=siege_tower)
        engineer_support.requires = RequiresPromotionComplete(promotion=catapult)
        demolition_expert.requires = RequiresPromotionComplete(promotion=engineer_support)

        self.add_promotion(promotion=battery_ram)
        self.add_promotion(promotion=artillery_barrage)
        self.add_promotion(promotion=siege_tower)
        self.add_promotion(promotion=catapult)
        self.add_promotion(promotion=engineer_support)
        self.add_promotion(promotion=demolition_expert)


class Seige(CoreMilitaryBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.seige",
            name=t_("content.units.classes.core.seige.name"),
            description=t_("content.units.classes.core.seige.description"),
            icon=None,
            *args,
            **kwargs,
        )
