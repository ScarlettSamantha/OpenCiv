from openciv.gameplay.culture import Civic
from openciv.engine.managers.i18n import _t


class TransparentGovernment(Civic):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="core.culture.civics.transparent_government",
            name=_t("content.culture.civics.core.transparent_government.name"),
            description=_t("content.culture.civics.core.transparent_government.description"),
            *args,
            **kwargs,
        )
