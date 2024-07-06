from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Printing(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.printing",
            _t("tech.printing.name"),
            _t("tech.printing.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
