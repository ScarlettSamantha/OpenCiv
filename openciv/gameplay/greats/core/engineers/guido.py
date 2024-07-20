from openciv.gameplay.greats.core.engineers._base import CoreBaseGreatEngineer
from openciv.engine.managers.i18n import _t


class Guido(CoreBaseGreatEngineer):
    def __init__(self):
        super().__init__(
            key="core.engineers.guido",
            name=_t("content.greats.core.people.guido_van_rossem.name"),
            description=_t("content.greats.core.people.guido_van_rossem.description"),
            cost=100,
        )
