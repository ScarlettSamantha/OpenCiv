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
                return ages[key]()
            except KeyError:
                raise TechNotFoundException(key)

        def add_to_space(self, classes, key, age) -> Tech:
            _class = get_tech(self, classes, key)
            self.add(_class)
            return _class(age=age)

        def add_age_to_space(self, ages, key) -> Tech:
            _class = get_age(self, ages, key)
            self._ages.append(_class)
            return _class

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
        construction: Tech = add_to_space(self, classes, "Construction", get_age(self, ages, "Classical"))

        apprenticeship: Tech = add_to_space(self, classes, "Apprenticeship", get_age(self, ages, "Medieval"))
        butress: Tech = add_to_space(self, classes, "Butress", get_age(self, ages, "Medieval"))
        education: Tech = add_to_space(self, classes, "Education", get_age(self, ages, "Medieval"))
        machinery: Tech = add_to_space(self, classes, "Machinery", get_age(self, ages, "Medieval"))
        stirrups: Tech = add_to_space(self, classes, "Stirrups", get_age(self, ages, "Medieval"))
        castles: Tech = add_to_space(self, classes, "Castles", get_age(self, ages, "Medieval"))
        military_engineering: Tech = add_to_space(self, classes, "MilitaryEngineering", get_age(self, ages, "Medieval"))
        military_tactics: Tech = add_to_space(self, classes, "MilitaryTactics", get_age(self, ages, "Medieval"))

        banking: Tech = add_to_space(self, classes, "Banking", get_age(self, ages, "Renaissance"))
        chemistry: Tech = add_to_space(self, classes, "Chemistry", get_age(self, ages, "Renaissance"))
        composites: Tech = add_to_space(self, classes, "Composites", get_age(self, ages, "Renaissance"))
        gunpowder: Tech = add_to_space(self, classes, "Gunpowder", get_age(self, ages, "Renaissance"))
        scientific_theory: Tech = add_to_space(self, classes, "ScientificTheory", get_age(self, ages, "Renaissance"))
        cartography: Tech = add_to_space(self, classes, "Cartography", get_age(self, ages, "Renaissance"))
        mass_production: Tech = add_to_space(self, classes, "MassProduction", get_age(self, ages, "Renaissance"))
        banking: Tech = add_to_space(self, classes, "Banking", get_age(self, ages, "Renaissance"))
        printing: Tech = add_to_space(self, classes, "Printing", get_age(self, ages, "Renaissance"))
        square_rigging: Tech = add_to_space(self, classes, "SquareRigging", get_age(self, ages, "Renaissance"))
        astronomy: Tech = add_to_space(self, classes, "Astronomy", get_age(self, ages, "Renaissance"))
        metal_casting: Tech = add_to_space(self, classes, "MetalCasting", get_age(self, ages, "Renaissance"))
        siege_tactics: Tech = add_to_space(self, classes, "SiegeTactics", get_age(self, ages, "Renaissance"))

        industrialisation: Tech = add_to_space(self, classes, "Industrialisation", get_age(self, ages, "Industrial"))
        mass_production: Tech = add_to_space(self, classes, "MassProduction", get_age(self, ages, "Industrial"))
        replaceable_parts: Tech = add_to_space(self, classes, "ReplacableParts", get_age(self, ages, "Industrial"))
        refining: Tech = add_to_space(self, classes, "Refining", get_age(self, ages, "Industrial"))
        steam_power: Tech = add_to_space(self, classes, "SteamPower", get_age(self, ages, "Industrial"))
        steel: Tech = add_to_space(self, classes, "Steel", get_age(self, ages, "Industrial"))
        ballistics: Tech = add_to_space(self, classes, "Ballistics", get_age(self, ages, "Industrial"))
        sanitation: Tech = add_to_space(self, classes, "Sanitation", get_age(self, ages, "Industrial"))
        economics: Tech = add_to_space(self, classes, "Economics", get_age(self, ages, "Industrial"))
        rifling: Tech = add_to_space(self, classes, "Rifling", get_age(self, ages, "Industrial"))

        combined_arms: Tech = add_to_space(self, classes, "CombinedArms", get_age(self, ages, "Modern"))
        advanced_ballistics: Tech = add_to_space(self, classes, "AdvancedBallistics", get_age(self, ages, "Modern"))
        advanced_flight: Tech = add_to_space(self, classes, "AdvancedFlight", get_age(self, ages, "Modern"))
        electricity: Tech = add_to_space(self, classes, "Electricity", get_age(self, ages, "Modern"))
        flight: Tech = add_to_space(self, classes, "Flight", get_age(self, ages, "Modern"))
        guidance_systems: Tech = add_to_space(self, classes, "GuidanceSystems", get_age(self, ages, "Modern"))
        lasers: Tech = add_to_space(self, classes, "Lasers", get_age(self, ages, "Modern"))
        rocketry: Tech = add_to_space(self, classes, "Rocketry", get_age(self, ages, "Modern"))
        satellites: Tech = add_to_space(self, classes, "Satellites", get_age(self, ages, "Modern"))
        stealth_technology: Tech = add_to_space(self, classes, "StealthTechnology", get_age(self, ages, "Modern"))
        synthetic_materials: Tech = add_to_space(self, classes, "SyntheticMaterials", get_age(self, ages, "Modern"))
        telecommunications: Tech = add_to_space(self, classes, "Telecommunications", get_age(self, ages, "Modern"))
        military_science: Tech = add_to_space(self, classes, "MilitaryScience", get_age(self, ages, "Modern"))

        nuclear_fission: Tech = add_to_space(self, classes, "NuclearFission", get_age(self, ages, "Modern"))
        plastics: Tech = add_to_space(self, classes, "Plastics", get_age(self, ages, "Modern"))
        radio: Tech = add_to_space(self, classes, "Radio", get_age(self, ages, "Modern"))
        combustion: Tech = add_to_space(self, classes, "Combustion", get_age(self, ages, "Modern"))
        computers: Tech = add_to_space(self, classes, "Computers", get_age(self, ages, "Modern"))

        nanotechnology: Tech = add_to_space(self, classes, "Nanotechnology", get_age(self, ages, "Information"))
        nuclear_fusion: Tech = add_to_space(self, classes, "NuclearFusion", get_age(self, ages, "Information"))
        robotoics: Tech = add_to_space(self, classes, "Robotics", get_age(self, ages, "Information"))

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

        calendar.requires = [clay_tablets]
        sailing.requires = [astrology]
        wheel.requires = [masonry]
        iron_working.requires = [bronze_working]
        mathematics.requires = [currency]

        ship_building.requires = [celestial_navigation]
        construction.requires = [wheel, horseback_riding]
        engineering.requires = [construction, mathematics, wheel]
        irrigation.requires = [calendar]

        butress.requires = [ship_building, mathematics]
        military_tactics.requires = [mathematics]
        construction.requires = [masonry]
        engineering.requires = [wheel]

        butress.requires = [ship_building]
        military_tactics.requires = [mathematics]
        apprenticeship.requires = [currency]
        machinery.requires = [engineering]

        education.requires = [mathematics]
        stirrups.requires = [horseback_riding]
        military_engineering.requires = [construction]
        castles.requires = [iron_working]

        cartography.requires = [butress]
        mass_production.requires = [military_tactics, education]
        banking.requires = [currency, education, stirrups]
        gunpowder.requires = [stirrups, education]
        printing.requires = [machinery]

        square_rigging.requires = [cartography]
        astronomy.requires = [education]
        metal_casting.requires = [gunpowder]
        siege_tactics.requires = [castles]

        industrialisation.requires = [mass_production, square_rigging]
        scientific_theory.requires = [astronomy, banking, metal_casting]
        ballistics.requires = [metal_casting]
        military_science.requires = [siege_tactics, printing]

        steam_power.requires = [industrialisation]
        sanitation.requires = [scientific_theory]
        economics.requires = [banking, metal_casting, scientific_theory]
        rifling.requires = [ballistics, military_science]

        flight.requires = [industrialisation]
        replaceable_parts.requires = [economics]
        steel.requires = [rifling]
        refining.requires = [rifling]

        electricity.requires = [steam_power]
        radio.requires = [flight, steam_power]
        chemistry.requires = [steel, replaceable_parts, sanitation]
        combustion.requires = [steel, refining]

        advanced_flight.requires = [radio]
        rocketry.requires = [chemistry, radio]
        advanced_ballistics.requires = [replaceable_parts, steel]
        combined_arms.requires = [steel, combustion]
        plastics.requires = [combustion]

        computers.requires = [electricity]
        nuclear_fusion.requires = [combined_arms, advanced_ballistics, rocketry]
        synthetic_materials.requires = [plastics]

        telecommunications.requires = [computers]
        satellites.requires = [rocketry, advanced_flight]
        guidance_systems.requires = [rocketry, advanced_ballistics]
        lasers.requires = [nuclear_fusion, advanced_ballistics]
        composites.requires = [synthetic_materials]
        stealth_technology.requires = [synthetic_materials]

        robotics = [computers, satellites, guidance_systems, lasers]
        nuclear_fission.requires = [lasers]
        nanotechnology.requires = [composites]

        all_techs = [
            hunting_gethering,
            trapping,
            animal_husbandry,
            bronze_working,
            pottery,
            writing,
            mining,
            archery,
            astrology,
            clay_tablets,
            sailing,
            masonry,
            calendar,
            wheel,
            irrigation,
            construction,
            currency,
            celestial_navigation,
            construction,
            engineering,
            mathematics,
            ship_building,
            horseback_riding,
            iron_working,
            construction,
            apprenticeship,
            butress,
            education,
            machinery,
            stirrups,
            castles,
            military_engineering,
            military_tactics,
            banking,
            chemistry,
            composites,
            gunpowder,
            scientific_theory,
            cartography,
            mass_production,
            banking,
            printing,
            square_rigging,
            astronomy,
            metal_casting,
            siege_tactics,
            industrialisation,
            mass_production,
            replaceable_parts,
            refining,
            steam_power,
            steel,
            ballistics,
            sanitation,
            economics,
            rifling,
            combined_arms,
            advanced_ballistics,
            advanced_flight,
            electricity,
            flight,
            guidance_systems,
            lasers,
            rocketry,
            satellites,
            stealth_technology,
            synthetic_materials,
            telecommunications,
            military_science,
            nuclear_fission,
            plastics,
            radio,
            combustion,
            computers,
            nanotechnology,
            nuclear_fusion,
            robotoics,
        ]

        self._items = all_techs


if __name__ == "__main__":
    core = Core()
    core.render()
