from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.mililtary._base import CoreMilitaryBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class PolicePromotion(Promotion):
    pass


class RiotControl(PolicePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.riot_control",
            name=t_("content.units.core.promotions.police.riot_control.name"),
            description=t_("content.units.core.promotions.police.riot_control.description"),
            *args,
            **kwargs,
        )


class Investigation(PolicePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.investigation",
            name=t_("content.units.core.promotions.police.investigation.name"),
            description=t_("content.units.core.promotions.police.investigation.description"),
            *args,
            **kwargs,
        )


class Patrol(PolicePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.patrol",
            name=t_("content.units.core.promotions.police.patrol.name"),
            description=t_("content.units.core.promotions.police.patrol.description"),
            *args,
            **kwargs,
        )


class SWATTraining(PolicePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.SWAT_training",
            name=t_("content.units.core.promotions.police.SWAT_training.name"),
            description=t_("content.units.core.promotions.police.SWAT_training.description"),
            *args,
            **kwargs,
        )


class CommunityOutreach(PolicePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.community_outreach",
            name=t_("content.units.core.promotions.police.community_outreach.name"),
            description=t_("content.units.core.promotions.police.community_outreach.description"),
            *args,
            **kwargs,
        )


class RapidResponse(PolicePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.rapid_response",
            name=t_("content.units.core.promotions.police.rapid_response.name"),
            description=t_("content.units.core.promotions.police.rapid_response.description"),
            *args,
            **kwargs,
        )


class PolicePromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.police", *args, **kwargs)

    def register_promotions(self) -> None:
        riot_control = RiotControl()
        investigation = Investigation()
        patrol = Patrol()
        SWAT_training = SWATTraining()
        community_outreach = CommunityOutreach()
        rapid_response = RapidResponse()

        riot_control.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        investigation.requires = RequiresPromotionComplete(promotion=riot_control)
        patrol.requires = RequiresPromotionComplete(promotion=investigation)
        SWAT_training.requires = RequiresPromotionComplete(promotion=patrol)
        community_outreach.requires = RequiresPromotionComplete(promotion=SWAT_training)
        rapid_response.requires = RequiresPromotionComplete(promotion=community_outreach)

        self.add_promotion(riot_control)
        self.add_promotion(investigation)
        self.add_promotion(patrol)
        self.add_promotion(SWAT_training)
        self.add_promotion(community_outreach)
        self.add_promotion(rapid_response)


class Police(CoreMilitaryBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.police",
            name=t_("content.units.classes.core.police.name"),
            description=t_("content.units.classes.core.police.description"),
            icon=None,
            *args,
            **kwargs,
        )
