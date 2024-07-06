from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Apprenticship(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.apprenticeship",
            _t("tech.apprenticeship.name"),
            _t("tech.apprenticeship.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
