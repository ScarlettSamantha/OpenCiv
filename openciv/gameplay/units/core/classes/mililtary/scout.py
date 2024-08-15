from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.mililtary._base import CoreMilitaryBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class ScoutPromotion(Promotion):
    pass


class Pathfinder(ScoutPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.pathfinder",
            name=t_("content.units.core.promotions.scout.pathfinder.name"),
            description=t_("content.units.core.promotions.scout.pathfinder.description"),
            *args,
            **kwargs,
        )


class Tracker(ScoutPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.tracker",
            name=t_("content.units.core.promotions.scout.tracker.name"),
            description=t_("content.units.core.promotions.scout.tracker.description"),
            *args,
            **kwargs,
        )


class Stealth(ScoutPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.stealth",
            name=t_("content.units.core.promotions.scout.stealth.name"),
            description=t_("content.units.core.promotions.scout.stealth.description"),
            *args,
            **kwargs,
        )


class Survivalist(ScoutPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.survivalist",
            name=t_("content.units.core.promotions.scout.survivalist.name"),
            description=t_("content.units.core.promotions.scout.survivalist.description"),
            *args,
            **kwargs,
        )


class Reconnaissance(ScoutPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.reconnaissance",
            name=t_("content.units.core.promotions.scout.reconnaissance.name"),
            description=t_("content.units.core.promotions.scout.reconnaissance.description"),
            *args,
            **kwargs,
        )


class SignalFlare(ScoutPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.signal_flare",
            name=t_("content.units.core.promotions.scout.signal_flare.name"),
            description=t_("content.units.core.promotions.scout.signal_flare.description"),
            *args,
            **kwargs,
        )


class ScoutPromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.scout", *args, **kwargs)

    def register_promotions(self) -> None:
        pathfinder = Pathfinder()
        tracker = Tracker()
        stealth = Stealth()
        survivalist = Survivalist()
        reconnaissance = Reconnaissance()
        signal_flare = SignalFlare()

        pathfinder.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        tracker.requires = RequiresPromotionComplete(promotion=pathfinder)
        stealth.requires = RequiresPromotionComplete(promotion=tracker)
        survivalist.requires = RequiresPromotionComplete(promotion=stealth)
        reconnaissance.requires = RequiresPromotionComplete(promotion=survivalist)
        signal_flare.requires = RequiresPromotionComplete(promotion=reconnaissance)

        self.add_promotion(promotion=pathfinder)
        self.add_promotion(promotion=tracker)
        self.add_promotion(promotion=stealth)
        self.add_promotion(promotion=survivalist)
        self.add_promotion(promotion=reconnaissance)
        self.add_promotion(promotion=signal_flare)


class Scout(CoreMilitaryBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.scout",
            name=t_("content.units.classes.core.scout.name"),
            description=t_("content.units.classes.core.scout.description"),
            icon=None,
            *args,
            **kwargs,
        )
