from __future__ import annotations

from openciv.engine.saving import SaveAble
from openciv.engine.managers.i18n import T_TranslationOrStr
from openciv.engine.requires import Requires
from openciv.gameplay.planes.plane import Plane
from openciv.gameplay.player import Player
from openciv.gameplay.promotion import PromotionTree
from openciv.gameplay.item import Items
from openciv.gameplay.combat.stats import Stats
from openciv.gameplay.units.classes._base import UnitBaseClass
from openciv.gameplay.resource import Costs
from openciv.gameplay.effect import Effects

from typing import Type, Any, List


class Unit(SaveAble):
    def __init__(
        self,
        key: str,
        name: T_TranslationOrStr,
        description: T_TranslationOrStr,
        max_health: int,
        attack: int,
        defense: int,
        base_movement: int,
        costs: Costs,
        health: int | None = None,
        armor_piercing: int = 0,
        attacks: int = 1,
        ammunition: int = -1,  # -1 means infinite
        seige_damage: int = 0,
        attack_range: int = 1,
        vision_range: int = 3,
        retaliation_modifier: int = 1,  # How much damage this unit does to units that attack it in melee, 0 means no retaliation
        can_fortify: bool = True,
        movement_modifier: int | float = 1,
        owner: Player | None = None,
        movement_left: int | None = None,
        promotion_tree: Type[PromotionTree] | None = None,
        auto_instance_promotions: bool = True,
        unit_class: Type[UnitBaseClass] | None = None,
        upgrades_from_class: bool = True,
        upgrades_to: Unit | None = None,
        upgrade_tier: int = 0,
        attackable_from_planes: List[Plane] = [],
        default_plane: Plane | None = None,
        can_attack_plane: Plane | None = None,
        current_plane: Plane | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.key: str = key
        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr = description

        self.owner: Player | None = owner  # The player that owns this unit.

        # Cost
        self.costs: Costs = costs

        # Movement Stats
        self.base_movement: int = base_movement
        self.movement_modifier: int | float = movement_modifier
        self.movement_left: float = base_movement if movement_left is None else movement_left
        self.is_fortified: bool = False

        self.can_raid: bool = False
        self.can_move: bool = True
        self.can_fortify: bool = can_fortify

        # Base Combat Stats these can be still modified by effects and equipment.
        self.health: int = max_health if health is None else health
        self.max_health: int = max_health
        self.attack: int = attack
        self.attacks: int = attacks  # How many times this unit can attack in a turn.
        self.defense: int = defense
        self.armor_piercing: int = armor_piercing
        self.ammunition: int = ammunition
        self.seige_damage: int = seige_damage  # How much damage this unit does to cities and fortifications.
        self.range: int = attack_range  # How far this unit can attack.
        self.vision_range: int = vision_range  # How far this unit can see.
        self.retaliation_bonus: int = retaliation_modifier

        self.indirect_fire: bool = False  # If this unit can fire over other units and terrain.

        self.calculated_attack: int = attack
        self.calculated_defense: int = defense
        self.calculated_armor_piercing: int = armor_piercing

        self.attacks_left: int = attacks  # How many attacks this unit has left in a turn.

        # Equipment
        self.weapons: Items = Items()
        self.armor: Items = Items()
        self.support: Items = Items()
        self.items: Items = Items()

        # Promotion
        self.unit_class: Type[UnitBaseClass] | None = unit_class
        self.promotion_tree_ref: Type[PromotionTree] | None = promotion_tree
        self.promotions: PromotionTree | None = None if promotion_tree is None else promotion_tree()  # type: ignore # noqa # We do this because we implement the arguments in a sub object so we dont have to pass them in every time.
        self.auto_instance_promotions: bool = auto_instance_promotions

        # Effects
        self.base_effects: Effects = Effects()
        self._effects: Effects | None = None

        # Combat Mechanical Links
        self.attackable_from_planes: List[Plane] = attackable_from_planes
        self.can_attack_plane: Plane | None = can_attack_plane

        self.default_plane: Plane | None = default_plane
        self.current_plane: Plane | None = current_plane

        self.needs_recalculation: bool = False

        # Upgrades
        self.upgrades_to: Unit | None = upgrades_to
        self.upgrades_from_class: bool = upgrades_from_class
        self.upgrade_tier: int = upgrade_tier
        self.upgrade_into_requirement: Requires = Requires()

    def __repr__(self) -> str:
        stats: dict[str, bool | int] = (
            self.promotions.stats() if self.promotions is not None else {"num_aquired": 0, "num_promotions": 0}
        )
        promotion_tree_name: T_TranslationOrStr = self.promotions.name if self.promotions is not None else "None"
        return f"{self.name}[{promotion_tree_name}|{stats['num_aquired']/stats['num_promotions']}]<{self.health}/{self.max_health}>[@{self.movement_remaining()}/{self.calculate_movement()}]"

    def plane(self) -> Plane | None:
        return self.current_plane

    def movement_remaining(self) -> float:
        return self.movement_left

    def calculate_movement(self) -> float:
        self.movement_left = self.base_movement + self.movement_modifier
        return self.movement_left

    def get_upgrade(self) -> Unit | None:
        if self.upgrades_to is not None:
            return self.upgrades_to
        return None

    def calculate_effects(self, calculate_promotions: bool = True, calculate_items: bool = True) -> None:
        self._effects = self.base_effects
        if calculate_promotions and self.promotions is not None:
            self._effects += self.promotions.effects
        if calculate_items:
            for category in (self.items, self.weapons, self.armor, self.support):
                for item in category:
                    if item.active and item.effects.__len__() > 0:
                        self._effects += item.effects

    def calculate_combat_stats(self):
        # Helper function to aggregate modifiers from items, promotions, and effects
        def aggregate_modifiers() -> Stats:
            base_stats: Stats = Stats(attack_modifier=0.0, defense_modifier=0.0, armor_piercing=0.0)

            # Aggregate item modifiers
            for item in self.items:
                if item.active:
                    base_stats = base_stats.add(other=item.combat_stats)

            # Aggregate promotion modifiers
            if self.promotions:
                base_stats = base_stats.add(other=self.promotions.combat_stats)

            # Aggregate effect modifiers
            if self._effects:
                base_stats = base_stats.add(other=self._effects.combat_stats)

            return base_stats

        # Get all modifiers
        modifiers: Stats = aggregate_modifiers()

        # Calculate final combat stats
        self.calculated_attack = round(float(self.attack) * float(modifiers.attack_modifier or 0.0))
        self.calculated_defense = round(float(self.defense) * float(modifiers.defense_modifier or 0.0))
        self.calculated_armor_piercing = round(float(self.armor_piercing) * float(modifiers.armor_piercing or 0.0))

    @property
    def effects(self) -> None | Effects:
        if self._effects is None:
            self.calculate_effects()
        return self._effects

    @effects.setter
    def effects(self, effects: Effects) -> None:
        self._effects = effects
