from openciv.gameplay.tile_modifiers import TileModifier
from openciv.gameplay.damage import DamageMode

# Some base modifiers these should match properties of the object.
walk = (TileModifier("walkable", True),)
no_walk = (TileModifier("walkable", False), TileModifier('movement_cost', 100))

no_sail = (TileModifier("sailable", False),)
sailable = (TileModifier('sailable', True),)

buildable = (TileModifier("buildable", True),)
not_buildable = (TileModifier("buildable", False),)

climbable = (TileModifier('climbable', True),)
no_climb = (TileModifier('climable', False),)

diggable = (TileModifier('diggable', True),)
no_diggable = (TileModifier('diggable', False),)

flyable = (TileModifier('flyable', True),)
no_flyable = (TileModifier('flyable', False),)

easily_traversable = (TileModifier('movement_cost', 1),)
hard_traversable = (TileModifier('movement_cost', 2),)

deep = (TileModifier('deep', True),)
shallow = (TileModifier('deep', False),)

growable = (TileModifier('growable', True),)
sterile = (TileModifier('growable', False),)

radiation_damage_per_turn = (TileModifier('damage_per_turn_on_units', 1), TileModifier('damage_per_turn_on_improvements_mode', DamageMode.DAMAGE_ABSOLUTE))

# Here we define some macro's so we dont have to reinvent everything everytime.
flat = easily_traversable + no_sail + no_climb
hilly = hard_traversable + no_sail + no_climb

not_traversable = no_walk + no_climb + no_sail + no_diggable

mountain = not_traversable + not_buildable + climbable

buildable_flat_land = no_sail + walk + buildable + no_climb + diggable + flyable + flat + growable
buildable_hills_land = no_sail + walk + buildable + no_climb + diggable + flyable + hilly + growable

flat_wasteland = sterile + radiation_damage_per_turn + walk + buildable + no_climb + diggable + flyable + flat
hills_wasteland = sterile + radiation_damage_per_turn + walk + buildable + no_climb + diggable + flyable + hilly
