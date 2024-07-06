from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class HorsebackRiding(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.horseback_riding",
            _t("tech.horseback_riding.name"),
            _t("tech.horseback_riding.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
