from __future__ import annotations
from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Liberalism(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.liberalism",
            name=_t("content.culture.subtrees.core.liberalism.name"),
            description=_t("content.culture.subtrees.core.liberalism.description"),
            *args,
            **kwargs,
        )

    def register_civics(self):
        from openciv.gameplay.cultures.core.individual_rights import IndividualRights
        from openciv.gameplay.cultures.core.free_market import FreeMarket
        from openciv.gameplay.cultures.core.representative_democracy import RepresentativeDemocracy
        from openciv.gameplay.cultures.core.social_welfare import SocialWelfare
        from openciv.gameplay.cultures.core.civil_liberties import CivilLiberties
        from openciv.gameplay.cultures.core.global_cooperation import GlobalCooperation
        from openciv.engine.requires import RequiresCivicComplete

        individual_rights = IndividualRights()
        self.add_civic(individual_rights)

        free_market = FreeMarket()
        free_market.requires = [RequiresCivicComplete(individual_rights)]
        self.add_civic(free_market)

        representative_democracy = RepresentativeDemocracy()
        representative_democracy.requires = [RequiresCivicComplete(individual_rights)]
        self.add_civic(representative_democracy)

        social_welfare = SocialWelfare()
        social_welfare.requires = [
            RequiresCivicComplete(free_market),
            RequiresCivicComplete(representative_democracy),
        ]
        self.add_civic(social_welfare)

        civil_liberties = CivilLiberties()
        civil_liberties.requires = [RequiresCivicComplete(individual_rights)]
        self.add_civic(civil_liberties)

        global_cooperation = GlobalCooperation()
        global_cooperation.requires = [
            RequiresCivicComplete(representative_democracy),
            RequiresCivicComplete(civil_liberties),
        ]
        self.add_civic(global_cooperation)
