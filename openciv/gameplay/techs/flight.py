from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Flight(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.flight",
            _t("tech.flight.name"),
            _t("tech.flight.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
