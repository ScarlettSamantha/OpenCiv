from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Nationalism(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.nationalism",
            name=_t("content.culture.subtrees.core.nationalism.name"),
            description=_t("content.culture.subtrees.core.nationalism.description"),
            *args,
            **kwargs,
        )

    def register_civics(self):
        from openciv.gameplay.cultures.core.patriotic_education import PatrioticEducation
        from openciv.gameplay.cultures.core.cultural_preservation import CulturalPreservation
        from openciv.gameplay.cultures.core.economic_nationalism import EconomicNationalism
        from openciv.gameplay.cultures.core.military_strength import MilitaryStrength
        from openciv.gameplay.cultures.core.national_sovereignty import NationalSovereignty
        from openciv.gameplay.cultures.core.national_unity import NationalUnity
        from openciv.engine.requires import RequiresCivicComplete

        patriotic_education = PatrioticEducation()
        self.add_civic(patriotic_education)

        cultural_preservation = CulturalPreservation()
        cultural_preservation.requires = [RequiresCivicComplete(patriotic_education)]
        self.add_civic(cultural_preservation)

        economic_nationalism = EconomicNationalism()
        economic_nationalism.requires = [RequiresCivicComplete(patriotic_education)]
        self.add_civic(economic_nationalism)

        military_strength = MilitaryStrength()
        military_strength.requires = [RequiresCivicComplete(cultural_preservation)]
        self.add_civic(military_strength)

        national_sovereignty = NationalSovereignty()
        national_sovereignty.requires = [
            RequiresCivicComplete(economic_nationalism),
            RequiresCivicComplete(military_strength),
        ]
        self.add_civic(national_sovereignty)

        national_unity = NationalUnity()
        national_unity.requires = [RequiresCivicComplete(national_sovereignty)]
        self.add_civic(national_unity)
