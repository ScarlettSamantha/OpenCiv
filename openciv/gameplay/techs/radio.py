from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Printing(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.radio",
            _t("tech.radio.name"),
            _t("tech.radio.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
