from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class CommunitySurveillance(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.community_surveillance",
            name=_t("content.culture.civics.core.community_surveillance.name"),
            description=_t("content.culture.civics.core.community_surveillance.description"),
            *args,
            **kwargs,
        )
