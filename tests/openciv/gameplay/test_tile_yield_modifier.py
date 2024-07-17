from openciv.gameplay.tile_yield_modifier import TileYieldModifier
from openciv.gameplay.tile_yield import TileYield

library = TileYield(science=1.0, mode=TileYield.ADDITIVE)

school = TileYield(science=2.0, mode=TileYield.ADDITIVE)

university = TileYield(science=2.0, mode=TileYield.PERCENTAGE_ADDATIVE)

hand_farm = TileYield(food=1.0, mode=TileYield.ADDITIVE)

animal_farm = TileYield(food=2.0, mode=TileYield.ADDITIVE)

furtalizer = TileYield(food=1.5, mode=TileYield.PERCENTAGE_CUMMULATIVE)


def test_science():
    set = TileYieldModifier()
    set.add(library)
    set.add(school)
    set.add(university)
    data = set.props()
    assert data.science == float(6)


def test_food():
    set = TileYieldModifier()
    set.add(hand_farm)
    set.add(animal_farm)
    set.add(furtalizer)
    data = set.props()
    assert data.food == float(4.5)
    assert type(data.food) == type(float())


def test_combined():
    set = TileYieldModifier()
    set.add(hand_farm)
    set.add(animal_farm)
    set.add(furtalizer)
    set.add(library)
    set.add(school)
    set.add(university)
    data = set.props()
    assert data.food == float(4.5)
    assert type(data.food) == type(float())
    assert data.science == float(6)
    assert type(data.science) == type(float())


if __name__ == "__main__":
    test_science()
    test_food()
    test_combined()
