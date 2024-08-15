from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.mililtary._base import CoreMilitaryBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class FrigatePromotion(Promotion):
    pass


class LongRangeBombartment(FrigatePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.long_range_bombardment",
            name=t_("content.units.core.promotions.frigate.long_range_bombardment.name"),
            description=t_("content.units.core.promotions.frigate.long_range_bombardment.description"),
            *args,
            **kwargs,
        )


class AntiAircraft(FrigatePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.anti_aircraft",
            name=t_("content.units.core.promotions.frigate.anti_aircraft.name"),
            description=t_("content.units.core.promotions.frigate.anti_aircraft.description"),
            *args,
            **kwargs,
        )


class ArmorPiercingShells(FrigatePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.armor_piercing_shells",
            name=t_("content.units.core.promotions.frigate.armor_piercing_shells.name"),
            description=t_("content.units.core.promotions.frigate.armor_piercing_shells.description"),
            *args,
            **kwargs,
        )


class RadarGuidance(FrigatePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.radar_guidance",
            name=t_("content.units.core.promotions.frigate.radar_guidance.name"),
            description=t_("content.units.core.promotions.frigate.radar_guidance.description"),
            *args,
            **kwargs,
        )


class Torpedoes(FrigatePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.torpedoes",
            name=t_("content.units.core.promotions.frigate.torpedoes.name"),
            description=t_("content.units.core.promotions.frigate.torpedoes.description"),
            *args,
            **kwargs,
        )


class FireSupression(FrigatePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.fire_supression",
            name=t_("content.units.core.promotions.frigate.fire_supression.name"),
            description=t_("content.units.core.promotions.frigate.fire_supression.description"),
            *args,
            **kwargs,
        )


class FrigatePromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.frigate", *args, **kwargs)

    def register_promotions(self):
        long_range_bombardment = LongRangeBombartment()
        anti_aircraft = AntiAircraft()
        armor_piercing_shells = ArmorPiercingShells()
        radar_guidance = RadarGuidance()
        torpedoes = Torpedoes()
        fire_supression = FireSupression()

        long_range_bombardment.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        anti_aircraft.requires = RequiresPromotionComplete(promotion=long_range_bombardment)
        armor_piercing_shells.requires = RequiresPromotionComplete(promotion=anti_aircraft)
        radar_guidance.requires = RequiresPromotionComplete(promotion=armor_piercing_shells)
        torpedoes.requires = RequiresPromotionComplete(promotion=radar_guidance)
        fire_supression.requires = RequiresPromotionComplete(promotion=torpedoes)

        self.add_promotion(promotion=long_range_bombardment)
        self.add_promotion(promotion=anti_aircraft)
        self.add_promotion(promotion=armor_piercing_shells)
        self.add_promotion(promotion=radar_guidance)
        self.add_promotion(promotion=torpedoes)
        self.add_promotion(promotion=fire_supression)


class Frigate(CoreMilitaryBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.frigate",
            name=t_("content.units.classes.core.frigate.name"),
            description=t_("content.units.classes.core.frigate.description"),
            icon=None,
            *args,
            **kwargs,
        )
