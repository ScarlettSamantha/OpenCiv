from openciv.gameplay.cultures.core.subs._base import BaseCoreSubtree
from openciv.engine.requires import RequiresCivicComplete
from openciv.engine.managers.i18n import _t


class Rationalism(BaseCoreSubtree):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.subtrees.rationalism",
            name=_t("content.culture.subtrees.core.rationalism.name"),
            description=_t("content.culture.subtrees.core.rationalism.description"),
            *args,
            **kwargs,
        )

    def register_civics(self):
        from openciv.gameplay.cultures.core.free_thought import FreeThought
        from openciv.gameplay.cultures.core.scientific_revolution import ScientificRevolution
        from openciv.gameplay.cultures.core.secularism import Secularism
        from openciv.gameplay.cultures.core.seperation_church_state import SeperationChurchState

        # Tier 1
        free_thought = FreeThought()
        secularism = Secularism()
        self.add_civic(free_thought)
        self.add_civic(secularism)

        # Tier 2
        scientific_revolution = ScientificRevolution()
        scientific_revolution.requires = [RequiresCivicComplete(free_thought), RequiresCivicComplete(secularism)]
        self.add_civic(scientific_revolution)

        # Tier 3
        seperation_church_state = SeperationChurchState()
        seperation_church_state.requires = [RequiresCivicComplete(scientific_revolution)]
        self.add_civic(seperation_church_state)
