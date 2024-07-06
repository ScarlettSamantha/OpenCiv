from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class SiegeTactics(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.siege_tactics",
            _t("tech.siege_tactics.name"),
            _t("tech.siege_tactics.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
