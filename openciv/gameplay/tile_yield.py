from openciv.engine.saving import SaveAble


class TileYield(SaveAble):
    BASE = 0
    ADDITIVE = 1

    PERCENTAGE_CUMMULATIVE = 2
    PERCENTAGE_ADDATIVE = 3

    MODE_STR = {
        BASE: "BASE",
        ADDITIVE: "ADDATIVE",
        PERCENTAGE_CUMMULATIVE: "PERCENTAGE_CUMMULATIVE",
        PERCENTAGE_ADDATIVE: "PERCENTAGE_ADDATIVE",
    }

    # Percentages need to be a 0.0 = 0 percentage in or decrease while 1.0 is a 100% increase and a -1.0 is a 100% decrease.
    # Absolute numbers are taken as a float but *should* be treated more like integers and are going to be rounded at the end.
    def __init__(
        self,
        name: str = None,
        gold: float = 0.0,
        production: float = 0.0,
        science: float = 0.0,
        food: float = 0.0,
        culture: float = 0.0,
        housing: float = 0.0,
        faith: float = 0.0,
        mode: int = ADDITIVE,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self._name = name
        self.mode = mode
        self.gold = gold
        self.production = production
        self.science = science
        self.food = food
        self.culture = culture
        self.housing = housing
        self.faith = faith

        self.content = 0.0
        self.angre = 0.0
        self.revolt = 0.0
        self.stability = 0.0

        self.great_person_science = 0
        self.great_person_production = 0
        self.great_person_admiral = 0
        self.great_person_marchant = 0
        self.great_person_leader = 0

        self._calculatable_properties = ("gold", "production", "science", "food", "culture", "housing", "faith")

        self._population_modifiers = ("content", "angre", "revolt", "stability")

        self._calculatable_great_people = ("science", "production", "admiral", "marchant", "leader")

        self._setup_saveable()

    @property
    def name(self) -> None | str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    def __repr__(self) -> str:
        return f"TileYield<Mode:{self.MODE_STR[self.mode]}>g:<{self.gold}>|p:<{self.production}>|s:<{self.science}>|f:<{self.food}>|c:<{self.culture}>|h:<{self.housing}>|fa:<{self.faith}>"

    def __add__(self, b: "TileYield") -> None:
        return self.add(b)

    def __mul__(self, b: "TileYield") -> None:
        return self.multiply(b)

    def set_prop(self, name: str, value: any):
        if name in self.calculatable_great_people() + self.calculatable_properties() + self.population_modifiers():
            raise ValueError(f"cannot set property[{name}] as it does not exist or is accessable")
        setattr(self, name, value)

    def add(self, tile_yield: "TileYield"):
        for property in self.calculatable_properties():
            addative_value = getattr(tile_yield, property)
            old_value = getattr(self, property)
            setattr(self, property, float(old_value + addative_value))
        for property in self.population_modifiers():
            addative_value = getattr(tile_yield, property)
            old_value = getattr(self, property)
            # Ensure both values are floats
            setattr(self, property, float(old_value + addative_value))
        for property in self.calculatable_great_people():
            addative_value = getattr(tile_yield, f"great_person_{property}")
            old_value = getattr(self, f"great_person_{property}")
            setattr(self, f"great_person_{property}", float(old_value + addative_value))
        return self

    def multiply(self, tile_yield: "TileYield"):
        for property in self.calculatable_properties():
            multiplicative_value = getattr(tile_yield, property)
            if multiplicative_value != 0.0:
                old_value = getattr(self, property)
                new_value = float(old_value * multiplicative_value)
                setattr(self, property, new_value)
        for property in self.population_modifiers():
            multiplicative_value = getattr(tile_yield, property)
            new_value = float(getattr(self, property) * multiplicative_value)
            setattr(self, property, new_value)
        for property in self.calculatable_great_people():
            multiplicative_value = getattr(tile_yield, f"great_person_{property}")
            new_value = float(getattr(self, f"great_person_{property}") * multiplicative_value)
            setattr(self, f"great_person_{property}", new_value)
        return self

    def calculate(self):
        pass

    def props(self):
        a = {}
        for item in self.calculatable_properties():
            a[item] = getattr(self, item)
        return a

    def convert_short_great_to_long(self, value: str) -> str:
        if value not in self.calculatable_great_people():
            raise TypeError(
                f"Cannot convert short to long name because great type does not seem to exist {type(value)}"
            )
        return f"great_person_{value}"

    def calculatable_properties(self):
        return self._calculatable_properties

    def population_modifiers(self):
        return self._population_modifiers

    def calculatable_great_people(self):
        return self._calculatable_great_people

    @staticmethod
    def baseYield() -> "TileYield":
        return TileYield()

    @staticmethod
    def nullYield() -> "TileYield":
        return TileYield(gold=0.0, production=0.0, science=0.0, food=0.0, culture=0.0, housing=0.0, faith=0.0)
