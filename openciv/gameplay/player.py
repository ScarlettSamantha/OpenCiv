from openciv.gameplay.civilization import Civilization
from openciv.gameplay.leader import Leader
from openciv.gameplay.personality import Personality
from openciv.gameplay.effects import Effects
from openciv.gameplay.effect import Effect
from openciv.gameplay.goverment import Goverment

from openciv.gameplay.mood import Mood
from openciv.gameplay.moods import Moods

from openciv.gameplay.relationships import Relationships

from openciv.gameplay.cities import Cities
from openciv.gameplay.city import City
from openciv.gameplay.tiles import Tiles
from openciv.gameplay.claims import Claims
from openciv.gameplay._units import Units
from openciv.gameplay.votes import Votes
from openciv.gameplay.citizens import Citizens

from openciv.gameplay.resource import Resources
from openciv.gameplay.great import Greats

from openciv.gameplay.trades import Trades

from openciv.ai.ai import AI


class Player:
    def __init__(
        self, name: str, turn_order: int, ai: AI, personality: Personality, civilization: Civilization, leader: Leader
    ):
        self.name: str = name
        self.ip: str | None = None
        self.identifier: str = None

        self.turn_order: int = turn_order

        self.is_human: int = 0
        self.is_being_controlled: int = 0
        self.instanace_controlling: int = 0

        self.ai: AI = ai
        self.personality: Personality = personality
        self.civilization: Civilization = civilization
        self.leader: Leader = leader

        self.mood: Mood = Mood()
        self.moods: Moods = Moods()
        self.relationships: Relationships = Relationships()

        self.focus = None
        self.commitment = 0
        self.goal = None

        self.war_readiness = 0
        self.war_exaustion = 0

        self.size_penalty = 0
        self.population_pentality = 0
        self.citizens: Citizens = Citizens()

        self.revolt = 0
        self.anarchy = 0
        self.subpression = 0
        self.popularity = 0
        self.taxes = 0

        self.police_effectiveness = 0
        self.counter_intelligence_effectiveness = 0

        self.goverment_strength = 0
        self.goverment: Goverment = Goverment()

        self.world_standing = 0
        self.delegates = 0

        self.cities: Cities = Cities()
        self.capital: City = None
        self.tiles: Tiles = Tiles()
        self.claims: Claims = Claims()
        self.units: Units = Units()
        self.votes: Votes = Votes()

        self.trades: Trades = Trades()

        self.resources: Resources = Resources()
        self.greats: Greats = Greats()

        self.effects: Effects = Effects()

        self._register_callbacks()

    def _register_callbacks(self):
        self.citizens.register_callback("on_birth", self.on_citizen_birth)

    def on_citizen_birth(self, citizen):
        self.population += 1

    def _recalculate(self):
        properties = ("citizens", "revolt", "anarchy", "subpression", "popularity")
        city_loop_needed: bool = False
        for prop in properties:
            if prop == "citizens":
                city_loop_needed = True
            else:
                pass

        def _city_loop(self):
            self.citizens.reset()
            for city in self.cities:
                self.citizens.create(num=city.population)

        if city_loop_needed:
            _city_loop(self)

    def getEffect(self, key):
        return self.effects.get(key)

    def getEffects(self):
        return self.effects

    def addEffect(self, key, effect: Effect):
        self.effects.add(key, effect)
