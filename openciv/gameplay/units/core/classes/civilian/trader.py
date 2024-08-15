from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.civilian._base import CoreCivilianBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class TraderPromotion(Promotion):
    pass


class Caravan(TraderPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.caravan",
            name=t_("content.units.core.promotions.trader.caravan.name"),
            description=t_("content.units.core.promotions.trader.caravan.description"),
            *args,
            **kwargs,
        )


class CargoShip(TraderPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.cargo_ship",
            name=t_("content.units.core.promotions.trader.cargo_ship.name"),
            description=t_("content.units.core.promotions.trader.cargo_ship.description"),
            *args,
            **kwargs,
        )


class Tycoon(TraderPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.tycoon",
            name=t_("content.units.core.promotions.trader.tycoon.name"),
            description=t_("content.units.core.promotions.trader.tycoon.description"),
            *args,
            **kwargs,
        )


class RailTycoon(TraderPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.rail_tycoon",
            name=t_("content.units.core.promotions.trader.rail_tycoon.name"),
            description=t_("content.units.core.promotions.trader.rail_tycoon.description"),
            *args,
            **kwargs,
        )


class OilTycoon(TraderPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.oil_tycoon",
            name=t_("content.units.core.promotions.trader.oil_tycoon.name"),
            description=t_("content.units.core.promotions.trader.oil_tycoon.description"),
            *args,
            **kwargs,
        )


class CorporateTycoon(TraderPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.corporate_tycoon",
            name=t_("content.units.core.promotions.trader.corporate_tycoon.name"),
            description=t_("content.units.core.promotions.trader.corporate_tycoon.description"),
            *args,
            **kwargs,
        )


class Industrialist(TraderPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.industrialist",
            name=t_("content.units.core.promotions.trader.industrialist.name"),
            description=t_("content.units.core.promotions.trader.industrialist.description"),
            *args,
            **kwargs,
        )


class Entrepreneur(TraderPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.entrepreneur",
            name=t_("content.units.core.promotions.trader.entrepreneur.name"),
            description=t_("content.units.core.promotions.trader.entrepreneur.description"),
            *args,
            **kwargs,
        )


class TraderPromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.trader", *args, **kwargs)

    def register_promotions(self):
        caravan = Caravan()
        cargo_ship = CargoShip()
        tycoon = Tycoon()
        rail_tycoon = RailTycoon()
        oil_tycoon = OilTycoon()
        corporate_tycoon = CorporateTycoon()
        industrialist = Industrialist()
        entrepreneur = Entrepreneur()

        caravan.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        cargo_ship.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        tycoon.requires = RequiresPromotionComplete(promotion=caravan)
        rail_tycoon.requires = RequiresPromotionComplete(promotion=tycoon)
        oil_tycoon.requires = RequiresPromotionComplete(promotion=tycoon)
        corporate_tycoon.requires = RequiresPromotionComplete(promotion=tycoon)
        industrialist.requires = RequiresPromotionComplete(promotion=tycoon)
        entrepreneur.requires = RequiresPromotionComplete(promotion=industrialist)

        self.add_promotion(promotion=caravan)
        self.add_promotion(promotion=cargo_ship)
        self.add_promotion(promotion=tycoon)
        self.add_promotion(promotion=rail_tycoon)
        self.add_promotion(promotion=oil_tycoon)
        self.add_promotion(promotion=corporate_tycoon)
        self.add_promotion(promotion=industrialist)
        self.add_promotion(promotion=entrepreneur)


class Trader(CoreCivilianBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.trader",
            name=t_("content.units.classes.core.trader.name"),
            description=t_("content.units.classes.core.trader.description"),
            icon=None,
            *args,
            **kwargs,
        )
