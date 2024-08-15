from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.mililtary._base import CoreMilitaryBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class CommandoPromotion(Promotion):
    pass


class GuerillaWarfare(CommandoPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.guerilla_warfare",
            name=t_("content.units.core.promotions.commando.guerilla_warfare.name"),
            description=t_("content.units.core.promotions.commando.guerilla_warfare.description"),
            *args,
            **kwargs,
        )


class Camouflage(CommandoPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.camouflage",
            name=t_("content.units.core.promotions.commando.camouflage.name"),
            description=t_("content.units.core.promotions.commando.camouflage.description"),
            *args,
            **kwargs,
        )


class Sabotage(CommandoPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.sabotage",
            name=t_("content.units.core.promotions.commando.sabotage.name"),
            description=t_("content.units.core.promotions.commando.sabotage.description"),
            *args,
            **kwargs,
        )


class Paratrooper(CommandoPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.paratrooper",
            name=t_("content.units.core.promotions.commando.paratrooper.name"),
            description=t_("content.units.core.promotions.commando.paratrooper.description"),
            *args,
            **kwargs,
        )


class SpecialForces(CommandoPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.special_forces",
            name=t_("content.units.core.promotions.commando.special_forces.name"),
            description=t_("content.units.core.promotions.commando.special_forces.description"),
            *args,
            **kwargs,
        )


class CommandoPromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.commando", *args, **kwargs)

    def register_promotions(self):
        guerilla_warfare = GuerillaWarfare(promotion_tree=self)
        camouflage = Camouflage(promotion_tree=self)
        sabotage = Sabotage(promotion_tree=self)
        paratrooper = Paratrooper(promotion_tree=self)
        special_forces = SpecialForces(promotion_tree=self)

        guerilla_warfare.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        camouflage.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        sabotage.requires = RequiresPromotionComplete(promotion=camouflage)
        paratrooper.requires = RequiresPromotionComplete(promotion=sabotage)
        special_forces.requires = RequiresPromotionComplete(promotion=paratrooper)

        self.add_promotion(promotion=guerilla_warfare)
        self.add_promotion(promotion=camouflage)
        self.add_promotion(promotion=sabotage)
        self.add_promotion(promotion=paratrooper)
        self.add_promotion(promotion=special_forces)


class Commando(CoreMilitaryBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.commando",
            name=t_("content.units.classes.core.commando.name"),
            description=t_("content.units.classes.core.commando.description"),
            icon=None,
            *args,
            **kwargs,
        )
