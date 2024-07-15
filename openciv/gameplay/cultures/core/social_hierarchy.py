from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class SocialHierarchy(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.social_hierarchy",
            name=_t("content.culture.civics.core.social_hierarchy.name"),
            description=_t("content.culture.civics.core.social_hierarchy.description"),
            *args,
            **kwargs,
        )
