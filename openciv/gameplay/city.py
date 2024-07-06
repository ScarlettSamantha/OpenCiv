from openciv.gameplay.improvements import Improvements
from openciv.gameplay.improvement import Improvement
from openciv.gameplay.citizens import Citizens


class City:
    def __init__(self, name: str, tile: "BaseTile"):  # noqa: F821
        self.name: str = name
        self.player: "Player" = tile.player  # noqa: F821
        self.tile: "BaseTile" = tile  # noqa: F821
        self.is_capital: bool = False

        self.active: bool = True
        self.destroyed: bool = False
        self.population: int = 1

        self.citizens: Citizens = Citizens()

        self.revolting: bool = False
        self.being_sieged: bool = False
        self.being_blockaded: bool = False

        self.health: int = 100
        self.max_health: int = 100

        self.tax_level: float = 0.0

        self._improvements: Improvements = Improvements()

        # @todo
        self.spies = []

        if self.player is not None:
            self._register_object()

    def build(self, improvement: Improvement):
        self._improvements.add(improvement)

    def promote_to_capital(self):
        self.is_capital = True

    def _register_object(self):
        self.player.cities.add(self)
        if self.is_capital:
            self.player.capital = self

    def birth(self, population: int = 1, *args, **kwargs):
        for i in range(population):
            self.citizens.create(*args, **kwargs)

    def _register_callbacks(self):
        self.citizens.register_callback("on_birth", self.on_citizen_birth)

    def on_citizen_birth(self, citizen):
        self.population += 1

    @classmethod
    def found_new(cls, name: str, tile: "BaseTile", population: int = 1, is_capital: bool = False) -> "City":  # noqa: F821
        instance = City(name=name, owner=tile.player)
        instance.tile = tile
        instance.population = population
        instance.is_capital = is_capital
        return instance
