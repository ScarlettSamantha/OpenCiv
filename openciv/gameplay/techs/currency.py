from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Currency(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.currency",
            _t("tech.currency.name"),
            _t("tech.currency.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
