from ursina import Entity, Vec3, MeshCollider
from ursina.shaders import lit_with_shadows_shader
from typing import List
from openciv.engine.managers.player import PlayerManager, Player
from openciv.gameplay.damage import DamageMode
from openciv.gameplay.units.baseunit import BaseUnit
from openciv.gameplay.tile_yield_modifier import TileYieldModifier, TileYield
from openciv.gameplay.improvements import Improvements
from openciv.gameplay.city import City
from openciv.world.items._base_item import BaseItem
from openciv.world.terrain._base_terrain import BaseTerrain
from openciv.world.weather._base_weather import BaseWeather
from openciv.world.features._base_feature import BaseFeature


class BaseTile:
    def __init__(self):
        self._reset_tile_properties_to_default()

    def _reset_tile_properties_to_default(self):
        # Has this tile been destroyed.
        self.destroyed = False
        self.grid_position = None
        self.raw_position = None

        # This is the height of the tile in relation to the average sea level in meters.
        self.gameplay_height = 0

        # Base health and if damagable declarations
        self.damagable = False
        self.health = 100
        self.damage = 0

        # Does it take damage over time ?
        self.damage_per_turn_mode = DamageMode.DAMAGE_NONE
        self.damage_per_turn = 0.0

        # Does it damage units over time ?
        self.damage_per_turn_on_units_mode = DamageMode.DAMAGE_NONE
        self.damage_per_turn_on_units = 0.0

        # Does it damamge improvements over time ?
        self.damage_per_turn_on_improvements_mode = DamageMode.DAMAGE_NONE
        self.damage_per_turn_on_improvements = 0.0

        # Can units walk over ?
        self.walkable = True
        # Can ships make it through ?
        self.sailable = False
        # Is this deep water ?
        self.deep = False
        # Can airplanes fly over ?
        self.flyable = True
        # Is space above accessable ?
        self.space_above = True
        # Can it be dug under ?
        self.diggable = True
        # Can it be build on ?
        self.buidable = True
        # If it can be walked over with clibing.
        self.climbable = True
        # If it can be claimed.
        self.claimable = True
        # If units can breeth
        self.air_breatheable = True
        # Can things grow on it ?
        self.growable = True

        # How difficult it is to move over this tile messured in movement cost (MC)
        self.movement_cost = 1.0

        # What kind of terrain does this have ?
        self.terrain: BaseTerrain = None
        # What weather is the tile having ?
        self.weather: BaseWeather = None

        # What features does this tile contain ?
        self.features: List[BaseFeature] = list()
        # Does this have any units ?
        self.units: List[BaseUnit] = list()
        # Does this have improvements ?
        self._improvements: Improvements = Improvements()
        # Does this have items sitting on top of it ?
        self.items: List[BaseItem] = list()
        # What kind of states apply to this object ?
        self.states = list()

        # Does this contain an city ?
        self.city: "City" | None = None
        # Who if anybody is the owner of this tile ?
        self.owner: Player = None
        # Who has claimed the tile but does not own it ?
        self.claimants = list()

        # We configure base tile yield mostly just for debugging.
        self.tile_yield: TileYieldModifier = TileYieldModifier(
            TileYield(gold=0.0, production=0.0, science=0.0, food=0.0, culture=0.0, housing=0.0),
            mode=TileYieldModifier.MODE_SET,
        )

        self.meshCollider = True

    def color(self):
        return self.terrain.fallback_color

    def model(self):
        return self.terrain.model()

    def texture(self):
        return self.terrain.texture()

    def setTerrain(self, terrain: BaseTerrain):
        self.terrain = terrain()

    def addTileYield(self, tileYield: TileYield):
        self.tile_yield += tileYield

    def tileYield(self):
        return self.tile_yield

    def improvements(self) -> Improvements:
        return self._improvements

    def build(self, improvement: "Improvement"):  # noqa: F821
        self._improvements.add(improvement)

    def found(self, player: Player = None, population: int = 1, capital: bool = False):
        if player is None:
            player = PlayerManager.player()
        self.city = City.found_new("Test city", player, self, population, capital)


class Tile(Entity):
    def __init__(self, tile: BaseTile, position: Vec3, x: int, y: int, **kwargs):
        self.tile = tile

        self._x = x
        self._y = y

        self.setup_tile()

        super().__init__(model=self.tile.model(), texture=self.tile.texture(), position=position, **kwargs)

        self.setup_colider()
        self.setup_shaders()

    def setup_tile(self):
        self.tile: BaseTile = self.tile()

    def setup_shaders(self):
        self.shader = lit_with_shadows_shader

    def setup_colider(self):
        if self.tile.meshCollider is True:
            self.collider = MeshCollider(self, mesh=self.model, center=Vec3(0, 0, 0))
