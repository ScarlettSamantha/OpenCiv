from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.mililtary._base import CoreMilitaryBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class MedicPromotion(Promotion):
    pass


class FieldMedic(MedicPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.field_medic",
            name=t_("content.units.core.promotions.medic.field_medic.name"),
            description=t_("content.units.core.promotions.medic.field_medic.description"),
            *args,
            **kwargs,
        )


class Triage(MedicPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.triage",
            name=t_("content.units.core.promotions.medic.triage.name"),
            description=t_("content.units.core.promotions.medic.triage.description"),
            *args,
            **kwargs,
        )


class FirstAid(MedicPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.first_aid",
            name=t_("content.units.core.promotions.medic.first_aid.name"),
            description=t_("content.units.core.promotions.medic.first_aid.description"),
            *args,
            **kwargs,
        )


class MobileHospital(MedicPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.mobile_hospital",
            name=t_("content.units.core.promotions.medic.mobile_hospital.name"),
            description=t_("content.units.core.promotions.medic.mobile_hospital.description"),
            *args,
            **kwargs,
        )


class CombatMedic(MedicPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.combat_medic",
            name=t_("content.units.core.promotions.medic.combat_medic.name"),
            description=t_("content.units.core.promotions.medic.combat_medic.description"),
            *args,
            **kwargs,
        )


class Evacuation(MedicPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.evacuation",
            name=t_("content.units.core.promotions.medic.evacuation.name"),
            description=t_("content.units.core.promotions.medic.evacuation.description"),
            *args,
            **kwargs,
        )


class MedicPromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.medic", *args, **kwargs)

    def register_promotions(self) -> None:
        field_medic = FieldMedic()
        triage = Triage()
        first_aid = FirstAid()
        mobile_hospital = MobileHospital()
        combat_medic = CombatMedic()
        evacuation = Evacuation()

        field_medic.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        triage.requires = RequiresPromotionComplete(promotion=field_medic)
        first_aid.requires = RequiresPromotionComplete(promotion=triage)
        mobile_hospital.requires = RequiresPromotionComplete(promotion=first_aid)
        combat_medic.requires = RequiresPromotionComplete(promotion=mobile_hospital)
        evacuation.requires = RequiresPromotionComplete(promotion=combat_medic)

        self.add_promotion(field_medic)
        self.add_promotion(triage)
        self.add_promotion(first_aid)
        self.add_promotion(mobile_hospital)
        self.add_promotion(combat_medic)
        self.add_promotion(evacuation)


class Medic(CoreMilitaryBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.medic",
            name=t_("content.units.classes.core.medic.name"),
            description=t_("content.units.classes.core.medic.description"),
            icon=None,
            *args,
            **kwargs,
        )
