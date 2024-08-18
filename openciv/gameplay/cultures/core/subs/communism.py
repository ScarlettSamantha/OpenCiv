from __future__ import annotations
from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Communism(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.communism",
            name=_t("content.culture.subtrees.core.communism.name"),
            description=_t("content.culture.subtrees.core.communism.description"),
            *args,
            **kwargs,
        )

    def register_civics(self):
        from openciv.gameplay.cultures.core.class_abolition import ClassAbolition
        from openciv.gameplay.cultures.core.communal_living import CommunalLiving
        from openciv.gameplay.cultures.core.centralized_economy import CentralizedEconomy
        from openciv.gameplay.cultures.core.proletarian_dictatorship import ProletarianDictatorship
        from openciv.gameplay.cultures.core.collectivized_agriculture import CollectivizedAgriculture
        from openciv.gameplay.cultures.core.international_solidarity import InternationalSolidarity
        from openciv.engine.requires import RequiresCivicComplete

        class_abolition = ClassAbolition()
        self.add_civic(class_abolition)

        communal_living = CommunalLiving()
        communal_living.requires = [RequiresCivicComplete(class_abolition)]
        self.add_civic(communal_living)

        centralized_economy = CentralizedEconomy()
        centralized_economy.requires = [RequiresCivicComplete(class_abolition)]
        self.add_civic(centralized_economy)

        proletarian_dictatorship = ProletarianDictatorship()
        proletarian_dictatorship.requires = [RequiresCivicComplete(communal_living)]
        self.add_civic(proletarian_dictatorship)

        collectivized_agriculture = CollectivizedAgriculture()
        collectivized_agriculture.requires = [
            RequiresCivicComplete(centralized_economy),
            RequiresCivicComplete(proletarian_dictatorship),
        ]
        self.add_civic(collectivized_agriculture)

        international_solidarity = InternationalSolidarity()
        international_solidarity.requires = [RequiresCivicComplete(collectivized_agriculture)]
        self.add_civic(international_solidarity)
