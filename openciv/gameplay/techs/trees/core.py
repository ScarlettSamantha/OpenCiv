from openciv.gameplay.tech import TechTree, Tech
from openciv.engine.managers.i18n import _t
from openciv.engine.exceptions.tech_exception import TechNotFoundException


class Core(TechTree):
    def __init__(self, *args, **kwargs):
        TechTree.__init__(
            self,
            name=_t("content.tech.trees.core.name"),
            description=_t("content.tech.trees.core.name"),
            icon=_t("content.tech.trees.core.icon"),
            *args,
            **kwargs,
        )
        self._add_items()

    def _add_items(self):
        from openciv.engine.additions.pyload import PyLoad

        classes = PyLoad.load_classes("openciv/gameplay/techs/")
        ages = PyLoad.load_classes("openciv/gameplay/ages/core/")

        # Just a type hint proxy
        def get_tech(self, classes, key) -> Tech:
            try:
                return classes[key]
            except KeyError:
                raise TechNotFoundException(key)

        def get_age(self, ages, key) -> Tech:
            try:
                return ages[key]
            except KeyError:
                raise TechNotFoundException(key)

        def add_to_space(self, classes, key, age) -> Tech:
            _class = get_tech(self, classes, key)
            self.add(_class)
            return _class(age=age)

        def add_age_to_space(self, ages, key) -> Tech:
            _class = get_age(self, ages, key)
            self._ages.append(_class)
            return _class()

        def load_ages(self, ages):
            ancient = add_age_to_space(self, ages, "Ancient")
            classical = add_age_to_space(self, ages, "Classical")
            medieval = add_age_to_space(self, ages, "Medieval")
            renaissance = add_age_to_space(self, ages, "Renaissance")
            industrial = add_age_to_space(self, ages, "Industrial")
            modern = add_age_to_space(self, ages, "Modern")
            atomic = add_age_to_space(self, ages, "Atomic")
            information = add_age_to_space(self, ages, "Information")
            future = add_age_to_space(self, ages, "Future")

            all_ages = [
                ancient,
                classical,
                medieval,
                renaissance,
                industrial,
                modern,
                atomic,
                information,
                future,
            ]

            self._ages = all_ages

        load_ages(self, ages)

        hunting_gethering: Tech = add_to_space(
            self, classes, "HuntingGethering", add_age_to_space(self, ages, "Ancient")
        )
        trapping: Tech = add_to_space(self, classes, "Trapping", get_age(self, ages, "Ancient"))
        animal_husbandry: Tech = add_to_space(self, classes, "AnimalHusbandry", get_age(self, ages, "Ancient"))
        bronze_working: Tech = add_to_space(self, classes, "BronzeWorking", get_age(self, ages, "Ancient"))
        pottery: Tech = add_to_space(self, classes, "Pottery", get_age(self, ages, "Ancient"))
        writing: Tech = add_to_space(self, classes, "Writing", get_age(self, ages, "Ancient"))
        mining: Tech = add_to_space(self, classes, "Mining", get_age(self, ages, "Ancient"))
        archery: Tech = add_to_space(self, classes, "Archery", get_age(self, ages, "Ancient"))

        astrology: Tech = add_to_space(self, classes, "Astrology", add_age_to_space(self, ages, "Classical"))
        clay_tablets: Tech = add_to_space(self, classes, "ClayTablets", get_age(self, ages, "Classical"))
        sailing: Tech = add_to_space(self, classes, "Sailing", get_age(self, ages, "Classical"))
        masonry: Tech = add_to_space(self, classes, "Masonry", get_age(self, ages, "Classical"))
        calendar: Tech = add_to_space(self, classes, "Calendar", get_age(self, ages, "Classical"))
        wheel: Tech = add_to_space(self, classes, "Wheel", get_age(self, ages, "Classical"))
        irrigation: Tech = add_to_space(self, classes, "Irrigation", get_age(self, ages, "Classical"))

        construction: Tech = add_to_space(self, classes, "Construction", get_age(self, ages, "Classical"))
        currency: Tech = add_to_space(self, classes, "Currency", get_age(self, ages, "Classical"))
        celestial_navigation: Tech = add_to_space(
            self, classes, "CelestialNavigation", get_age(self, ages, "Classical")
        )
        construction: Tech = add_to_space(self, classes, "Construction", get_age(self, ages, "Classical"))
        engineering: Tech = add_to_space(self, classes, "Engineering", get_age(self, ages, "Classical"))
        mathematics: Tech = add_to_space(self, classes, "Mathematics", get_age(self, ages, "Classical"))
        ship_building: Tech = add_to_space(self, classes, "ShipBuilding", get_age(self, ages, "Classical"))
        horseback_riding: Tech = add_to_space(self, classes, "HorsebackRiding", get_age(self, ages, "Classical"))
        iron_working: Tech = add_to_space(self, classes, "IronWorking", get_age(self, ages, "Classical"))

        animal_husbandry.requires = [hunting_gethering]
        pottery.requires = [hunting_gethering]
        mining.requires = [hunting_gethering]
        trapping.requires = [hunting_gethering]

        archery.requires = [hunting_gethering, trapping]
        writing.requires = [pottery]
        astrology.requires = [pottery]
        masonry.requires = [pottery, mining]
        bronze_working.requires = [mining]

        currency.requires = [writing]
        celestial_navigation.requires = [sailing, writing]
        clay_tablets.requires = [writing]
        horseback_riding.requires = [animal_husbandry, archery]
        ship_building.requires = [celestial_navigation]

        calendar.requires = [clay_tablets]
        sailing.requires = [astrology]
        wheel.requires = [masonry]
        iron_working.requires = [bronze_working]
        mathematics.requires = [currency]

        construction.requires = [wheel, horseback_riding]
        engineering.requires = [construction, mathematics, wheel]
        irrigation.requires = [calendar]

        all_techs = [
            hunting_gethering,
            trapping,
            animal_husbandry,
            pottery,
            writing,
            mining,
            archery,
            clay_tablets,
            sailing,
            masonry,
            calendar,
            wheel,
            irrigation,
            astrology,
            engineering,
            construction,
            mathematics,
            iron_working,
            ship_building,
            horseback_riding,
            celestial_navigation,
            bronze_working,
            currency,
        ]

        self._items = all_techs


if __name__ == "__main__":
    core = Core()
    core.render()
