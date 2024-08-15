from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.mililtary._base import CoreMilitaryBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class MelePromotion(Promotion):
    pass


class Beserk(MelePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.berserk",
            name=t_("content.units.core.promotions.mele.berserk.name"),
            description=t_("content.units.core.promotions.mele.berserk.description"),
            *args,
            **kwargs,
        )


class ShieldWall(MelePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.shield_wall",
            name=t_("content.units.core.promotions.mele.shield_wall.name"),
            description=t_("content.units.core.promotions.mele.shield_wall.description"),
            *args,
            **kwargs,
        )


class DualWielding(MelePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.dual_wielding",
            name=t_("content.units.core.promotions.mele.dual_wielding.name"),
            description=t_("content.units.core.promotions.mele.dual_wielding.description"),
            *args,
            **kwargs,
        )


class BattleHardened(MelePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.battle_hardened",
            name=t_("content.units.core.promotions.mele.battle_hardened.name"),
            description=t_("content.units.core.promotions.mele.battle_hardened.description"),
            *args,
            **kwargs,
        )


class Cleave(MelePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.cleave",
            name=t_("content.units.core.promotions.mele.cleave.name"),
            description=t_("content.units.core.promotions.mele.cleave.description"),
            *args,
            **kwargs,
        )


class DefensiveStance(MelePromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.defensive_stance",
            name=t_("content.units.core.promotions.mele.defensive_stance.name"),
            description=t_("content.units.core.promotions.mele.defensive_stance.description"),
            *args,
            **kwargs,
        )


class MelePromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.mele", *args, **kwargs)

    def register_promotions(self) -> None:
        bezerk = Beserk()
        shield_wall = ShieldWall()
        dual_wielding = DualWielding()
        battle_hardened = BattleHardened()
        cleave = Cleave()
        defensive_stance = DefensiveStance()

        bezerk.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        shield_wall.requires = RequiresPromotionComplete(promotion=bezerk)
        dual_wielding.requires = RequiresPromotionComplete(promotion=shield_wall)
        battle_hardened.requires = RequiresPromotionComplete(promotion=dual_wielding)
        cleave.requires = RequiresPromotionComplete(promotion=battle_hardened)
        defensive_stance.requires = RequiresPromotionComplete(promotion=cleave)

        self.add_promotion(promotion=bezerk)
        self.add_promotion(promotion=shield_wall)
        self.add_promotion(promotion=dual_wielding)
        self.add_promotion(promotion=battle_hardened)
        self.add_promotion(promotion=cleave)
        self.add_promotion(promotion=defensive_stance)


class Mele(CoreMilitaryBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.mele",
            name=t_("content.units.classes.core.mele.name"),
            description=t_("content.units.classes.core.mele.description"),
            icon=None,
            *args,
            **kwargs,
        )
