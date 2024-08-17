from __future__ import annotations

from openciv.engine.saving import SaveAble
from openciv.gameplay.resource import Resource
from openciv.gameplay.resources.core.basic.culture import Culture
from openciv.gameplay.resources.core.basic.faith import Faith
from openciv.gameplay.resources.core.basic.food import Food
from openciv.gameplay.resources.core.basic.gold import Gold
from openciv.gameplay.resources.core.basic.housing import Housing
from openciv.gameplay.resources.core.basic.production import Production
from openciv.gameplay.resources.core.basic.science import Science

from openciv.gameplay.resources.core.mechanics.stability import Stability
from openciv.gameplay.resources.core.mechanics.contentment import Contentment
from openciv.gameplay.resources.core.mechanics.angre import Angre
from openciv.gameplay.resources.core.mechanics.revolt import Revolt

from openciv.gameplay.resources.core.mechanics.greats import (
    GreatArtist,
    GreatCommerece,
    GreatMilitary,
    GreatEngineer,
    GreatScientist,
    GreatHero,
    GreatHoly,
)

from typing import Dict, List, Any, Self


class TileYield(SaveAble):
    BASE = 0
    ADDITIVE = 1

    PERCENTAGE_CUMMULATIVE = 2
    PERCENTAGE_ADDATIVE = 3

    MODE_STR: Dict[int, str] = {
        BASE: "BASE",
        ADDITIVE: "ADDATIVE",
        PERCENTAGE_CUMMULATIVE: "PERCENTAGE_CUMMULATIVE",
        PERCENTAGE_ADDATIVE: "PERCENTAGE_ADDATIVE",
    }

    # Percentages need to be a 0.0 = 0 percentage in or decrease while 1.0 is a 100% increase and a -1.0 is a 100% decrease.
    # Absolute numbers are taken as a float but *should* be treated more like integers and are going to be rounded at the end.
    def __init__(
        self,
        name: str | None = None,
        gold: float = 0.0,
        production: float = 0.0,
        science: float = 0.0,
        food: float = 0.0,
        culture: float = 0.0,
        housing: float = 0.0,
        faith: float = 0.0,
        mode: int = ADDITIVE,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self._name: str | None = name
        self.mode: int = mode
        self.gold: Gold = Gold(value=gold)
        self.production: Production = Production(value=production)
        self.science: Science = Science(value=science)
        self.food: Food = Food(value=food)
        self.culture: Culture = Culture(value=culture)
        self.housing: Housing = Housing(value=housing)
        self.faith: Faith = Faith(value=faith)

        self.contentment: Contentment = Contentment(value=0.0)
        self.angre: Angre = Angre(value=0.0)
        self.revolt: Revolt = Revolt(value=0.0)
        self.stability: Stability = Stability(value=0.0)

        self.great_person_science: GreatScientist = GreatScientist(value=0.0)
        self.great_person_production: GreatEngineer = GreatEngineer(value=0.0)
        self.great_person_artist: GreatArtist = GreatArtist(value=0.0)
        self.great_person_military: GreatMilitary = GreatMilitary(value=0.0)
        self.great_person_commerce: GreatCommerece = GreatCommerece(value=0.0)
        self.great_person_hero: GreatHero = GreatHero(value=0.0)
        self.great_person_holy: GreatHoly = GreatHoly(value=0.0)

        self._calculatable_properties: List[str] = [
            "gold",
            "production",
            "science",
            "food",
            "culture",
            "housing",
            "faith",
        ]
        self._mechanic_resources: List[str] = ["contentment", "angre", "revolt", "stability"]
        self._calculatable_great_people: List[str] = [
            "science",
            "production",
            "artist",
            "military",
            "commerce",
            "hero",
            "holy",
        ]

        self.other_mechnics: Dict[str, Resource] = {}

        self._setup_saveable()

    @property
    def name(self) -> None | str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    def __repr__(self) -> str:
        return f"TileYield<Mode:{self.MODE_STR[self.mode]}>g:<{self.gold}>|p:<{self.production}>|s:<{self.science}>|f:<{self.food}>|c:<{self.culture}>|h:<{self.housing}>|fa:<{self.faith}>"

    def __add__(self, b: TileYield) -> Self:
        return self.add(tile_yield=b)

    def __mul__(self, b: TileYield) -> Self:
        return self.multiply(tile_yield=b)

    def set_prop(self, name: str, value: Any):
        if name in self.calculatable_great_people() + self.calculatable_properties():
            raise ValueError(f"cannot set property[{name}] as it does not exist or is accessable")
        setattr(self, name, value)

    def add(self, tile_yield: TileYield) -> Self:
        for property in self.calculatable_properties():
            addative_value = getattr(tile_yield, property)
            old_value = getattr(self, property)
            setattr(self, property, old_value + addative_value)
        for property in self.mechanic_resources():
            addative_value = getattr(tile_yield, property)
            old_value = getattr(self, property)
            # Ensure both values are floats
            setattr(self, property, old_value + addative_value)
        for property in self.calculatable_great_people():
            addative_value = getattr(tile_yield, f"great_person_{property}")
            old_value = getattr(self, f"great_person_{property}")
            setattr(self, f"great_person_{property}", old_value + addative_value)
        for key, mechanic in self.other_mechnics.items():
            # Property is not in the other object so no operation.
            if key not in tile_yield.other_mechnics.keys():
                continue
            addative_value = getattr(tile_yield, str(mechanic))
            self.other_mechnics[key] = tile_yield.other_mechnics[key] + addative_value
        return self

    def multiply(self, tile_yield: TileYield) -> Self:
        for property in self.calculatable_properties():
            multiplicative_value = getattr(tile_yield, property)
            if (
                multiplicative_value == 0.0
                or multiplicative_value == 1.0
                or multiplicative_value == -1.0
                or multiplicative_value == 0
                or (hasattr(multiplicative_value, "value") and multiplicative_value.value == 0.0)
            ):
                continue
            old_value = getattr(self, property)
            new_value = old_value * multiplicative_value
            setattr(self, property, new_value)
        for property in self.mechanic_resources():
            multiplicative_value = getattr(tile_yield, property)
            new_value = getattr(self, property) * multiplicative_value
            setattr(self, property, new_value)
        for property in self.calculatable_great_people():
            multiplicative_value = getattr(tile_yield, f"great_person_{property}")
            new_value = getattr(self, f"great_person_{property}") * multiplicative_value
            setattr(self, f"great_person_{property}", new_value)
        for key, mechanic in self.other_mechnics.items():
            # Property is not in the other object so no operation.
            if key not in tile_yield.other_mechnics.keys():
                continue
            multiplicative_value = getattr(tile_yield, str(mechanic))
            self.other_mechnics[key] = tile_yield.other_mechnics[key] * multiplicative_value
        return self

    def calculate(self) -> None:
        pass

    def props(self) -> Dict[Any, Any]:
        a: Dict[Any, Any] = {}
        for item in self.calculatable_properties():
            a[item] = getattr(self, item)
        return a

    def convert_short_great_to_long(self, value: str) -> str:
        if value not in self.calculatable_great_people():
            raise TypeError(
                f"Cannot convert short to long name because great type does not seem to exist {type(value)}"
            )
        return f"great_person_{value}"

    def calculatable_properties(self) -> List[str]:
        return self._calculatable_properties

    def mechanic_resources(self) -> List[str]:
        return self._mechanic_resources

    def calculatable_great_people(self) -> List[str]:
        return self._calculatable_great_people

    @staticmethod
    def baseYield() -> TileYield:
        return TileYield()

    @staticmethod
    def nullYield() -> TileYield:
        return TileYield(gold=0.0, production=0.0, science=0.0, food=0.0, culture=0.0, housing=0.0, faith=0.0)
