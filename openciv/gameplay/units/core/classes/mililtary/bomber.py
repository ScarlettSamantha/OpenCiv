from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.mililtary._base import CoreMilitaryBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class BomberPromotion(Promotion):
    pass


class AirRepair(BomberPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.air_repair",
            name=t_("content.units.core.promotions.bomber.air_repair.name"),
            description=t_("content.units.core.promotions.bomber.air_repair.description"),
            *args,
            **kwargs,
        )


class JetEngine(BomberPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.jet_engine",
            name=t_("content.units.core.promotions.bomber.jet_engine.name"),
            description=t_("content.units.core.promotions.bomber.jet_engine.description"),
            *args,
            **kwargs,
        )


class UpgradedBombbays(BomberPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.upgraded_bombbays",
            name=t_("content.units.core.promotions.bomber.upgraded_bombbays.name"),
            description=t_("content.units.core.promotions.bomber.upgraded_bombbays.description"),
            *args,
            **kwargs,
        )


class Flares(BomberPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.flares",
            name=t_("content.units.core.promotions.bomber.flares.name"),
            description=t_("content.units.core.promotions.bomber.flares.description"),
            *args,
            **kwargs,
        )


class ActiveRadarJamming(BomberPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.active_radar_jamming",
            name=t_("content.units.core.promotions.bomber.air_repair.name"),
            description=t_("content.units.core.promotions.bomber.air_repair.description"),
            *args,
            **kwargs,
        )


class GlideBombing(BomberPromotion):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.promotion.glide_bombing",
            name=t_("content.units.core.promotions.bomber.glide_bombing.name"),
            description=t_("content.units.core.promotions.bomber.glide_bombing.description"),
            *args,
            **kwargs,
        )


class BomberPromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.bomber", *args, **kwargs)

    def register_promotions(self):
        air_repair = AirRepair()
        jet_engine = JetEngine()
        upgraded_bombbays = UpgradedBombbays()
        flares = Flares()
        active_radar_jamming = ActiveRadarJamming()
        glide_bombing = GlideBombing()

        air_repair.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        jet_engine.requires = RequiresPromotionComplete(promotion=air_repair)
        upgraded_bombbays.requires = RequiresPromotionComplete(promotion=jet_engine)
        flares.requires = RequiresPromotionComplete(promotion=upgraded_bombbays)
        active_radar_jamming.requires = RequiresPromotionComplete(promotion=flares)
        glide_bombing.requires = RequiresPromotionComplete(promotion=active_radar_jamming)

        self.add_promotion(promotion=air_repair)
        self.add_promotion(promotion=jet_engine)
        self.add_promotion(promotion=upgraded_bombbays)
        self.add_promotion(promotion=flares)
        self.add_promotion(promotion=active_radar_jamming)
        self.add_promotion(promotion=glide_bombing)


class Bomber(CoreMilitaryBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.bomber",
            name=t_("content.units.classes.core.bomber.name"),
            description=t_("content.units.classes.core.bomber.description"),
            icon=None,
            *args,
            **kwargs,
        )
