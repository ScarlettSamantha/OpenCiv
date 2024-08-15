from __future__ import annotations
from typing import Any


class Stats:
    def __init__(
        self,
        attack_modifier: float | None = None,
        defense_modifier: float | None = None,
        armor_piercing: float | None = None,
    ) -> None:
        self.attack_modifier: float | None = attack_modifier
        self.defense_modifier: float | None = defense_modifier
        self.armor_piercing: float | None = armor_piercing

    def add(self, other: Stats) -> Stats:
        """
        Combines this Stats object with another, summing their modifiers.
        """
        return Stats(
            attack_modifier=(self.attack_modifier or 0.0) + (other.attack_modifier or 0.0),
            defense_modifier=(self.defense_modifier or 0.0) + (other.defense_modifier or 0.0),
            armor_piercing=(self.armor_piercing or 0.0) + (other.armor_piercing or 0.0),
        )

    def __add__(self, other: Stats) -> Stats:
        return self.add(other=other)

    def __iadd__(self, other: Stats) -> Stats:
        combined: Stats = self.add(other=other)
        self.attack_modifier = combined.attack_modifier
        self.defense_modifier = combined.defense_modifier
        self.armor_piercing = combined.armor_piercing
        return self

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Stats):
            return False
        return (
            self.attack_modifier == other.attack_modifier
            and self.defense_modifier == other.defense_modifier
            and self.armor_piercing == other.armor_piercing
        )

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other=other)

    def __lt__(self, other: Stats) -> bool:
        return (
            (self.attack_modifier or 0.0) < (other.attack_modifier or 0.0)
            and (self.defense_modifier or 0.0) < (other.defense_modifier or 0.0)
            and (self.armor_piercing or 0.0) < (other.armor_piercing or 0.0)
        )

    def __le__(self, other: Stats) -> bool:
        return self.__lt__(other=other) or self.__eq__(other=other)

    def __gt__(self, other: Stats) -> bool:
        return (
            (self.attack_modifier or 0.0) > (other.attack_modifier or 0.0)
            and (self.defense_modifier or 0.0) > (other.defense_modifier or 0.0)
            and (self.armor_piercing or 0.0) > (other.armor_piercing or 0.0)
        )

    def __ge__(self, other: Stats) -> bool:
        return self.__gt__(other=other) or self.__eq__(other=other)

    def __repr__(self) -> str:
        return (
            f"Stats(attack_modifier={self.attack_modifier}, "
            f"defense_modifier={self.defense_modifier}, "
            f"armor_piercing={self.armor_piercing})"
        )

    def __str__(self) -> str:
        return (
            f"Attack: {self.attack_modifier}, Defense: {self.defense_modifier}, "
            f"Armor Piercing: {self.armor_piercing}"
        )

    def __bool__(self) -> bool:
        return bool(self.attack_modifier or 0) or bool(self.defense_modifier or 0) or bool(self.armor_piercing or 0)
