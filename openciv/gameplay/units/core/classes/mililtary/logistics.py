from __future__ import annotations
from typing import Any
from openciv.engine.managers.i18n import t_

from openciv.gameplay.units.core.classes.mililtary._base import CoreMilitaryBaseClass
from openciv.gameplay.promotion import Promotion, PromotionTree
from openciv.engine.requires import RequiresPromotionComplete, RequiresPromotionTreeUnlocked


class LogisticsPromotion(Promotion):
    pass


class SupplyChain(LogisticsPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.supply_chain",
            name=t_("content.units.core.promotions.logistics.supply_chain.name"),
            description=t_("content.units.core.promotions.logistics.supply_chain.description"),
            *args,
            **kwargs,
        )


class QuickRepair(LogisticsPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.quick_repair",
            name=t_("content.units.core.promotions.logistics.quick_repair.name"),
            description=t_("content.units.core.promotions.logistics.quick_repair.description"),
            *args,
            **kwargs,
        )


class AmmunitionTransport(LogisticsPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.ammunition_transport",
            name=t_("content.units.core.promotions.logistics.ammunition_transport.name"),
            description=t_("content.units.core.promotions.logistics.ammunition_transport.description"),
            *args,
            **kwargs,
        )


class FuelEfficiency(LogisticsPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.fuel_efficiency",
            name=t_("content.units.core.promotions.logistics.fuel_efficiency.name"),
            description=t_("content.units.core.promotions.logistics.fuel_efficiency.description"),
            *args,
            **kwargs,
        )


class MedicalSupplies(LogisticsPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.medical_supplies",
            name=t_("content.units.core.promotions.logistics.medical_supplies.name"),
            description=t_("content.units.core.promotions.logistics.medical_supplies.description"),
            *args,
            **kwargs,
        )


class CommunicationNetwork(LogisticsPromotion):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(
            key="core.unit.promotion.communication_network",
            name=t_("content.units.core.promotions.logistics.communication_network.name"),
            description=t_("content.units.core.promotions.logistics.communication_network.description"),
            *args,
            **kwargs,
        )


class LogisticsPromotionTree(PromotionTree):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="core.unit.promotion.tree.logistics", *args, **kwargs)

    def register_promotions(self):
        supply_chain = SupplyChain()
        quick_repair = QuickRepair()
        ammunition_transport = AmmunitionTransport()
        fuel_efficiency = FuelEfficiency()
        medical_supplies = MedicalSupplies()
        communication_network = CommunicationNetwork()

        supply_chain.requires = RequiresPromotionTreeUnlocked(promotion_tree=self)
        quick_repair.requires = RequiresPromotionComplete(promotion=supply_chain)
        ammunition_transport.requires = RequiresPromotionComplete(promotion=quick_repair)
        fuel_efficiency.requires = RequiresPromotionComplete(promotion=ammunition_transport)
        medical_supplies.requires = RequiresPromotionComplete(promotion=fuel_efficiency)
        communication_network.requires = RequiresPromotionComplete(promotion=medical_supplies)

        self.add_promotion(supply_chain)
        self.add_promotion(quick_repair)
        self.add_promotion(ammunition_transport)
        self.add_promotion(fuel_efficiency)
        self.add_promotion(medical_supplies)
        self.add_promotion(communication_network)


class Logistics(CoreMilitaryBaseClass):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(
            key="core.unit.class.logistics",
            name=t_("content.units.classes.core.logistics.name"),
            description=t_("content.units.classes.core.logistics.description"),
            icon=None,
            *args,
            **kwargs,
        )
