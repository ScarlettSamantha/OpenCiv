from __future__ import annotations
from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.managers.i18n import _t


class Socialism(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.socialism",
            name=_t("content.culture.subtrees.core.socialism.name"),
            description=_t("content.culture.subtrees.core.socialism.description"),
            *args,
            **kwargs,
        )

    def register_civics(self):
        from openciv.gameplay.cultures.core.collective_ownership import CollectiveOwnership
        from openciv.gameplay.cultures.core.workers_rights import WorkersRights
        from openciv.gameplay.cultures.core.universal_healthcare import UniversalHealthcare
        from openciv.gameplay.cultures.core.free_education import FreeEducation
        from openciv.gameplay.cultures.core.social_equality import SocialEquality
        from openciv.gameplay.cultures.core.state_planning import StatePlanning
        from openciv.engine.requires import RequiresCivicComplete

        collective_ownership = CollectiveOwnership()
        self.add_civic(collective_ownership)

        workers_rights = WorkersRights()
        workers_rights.requires = [RequiresCivicComplete(collective_ownership)]
        self.add_civic(workers_rights)

        universal_healthcare = UniversalHealthcare()
        universal_healthcare.requires = [RequiresCivicComplete(workers_rights)]
        self.add_civic(universal_healthcare)

        free_education = FreeEducation()
        free_education.requires = [RequiresCivicComplete(collective_ownership)]
        self.add_civic(free_education)

        social_equality = SocialEquality()
        social_equality.requires = [
            RequiresCivicComplete(universal_healthcare),
            RequiresCivicComplete(free_education),
        ]
        self.add_civic(social_equality)

        state_planning = StatePlanning()
        state_planning.requires = [RequiresCivicComplete(social_equality)]
        self.add_civic(state_planning)
