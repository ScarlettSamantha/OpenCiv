from openciv.gameplay.tech import Tech
from openciv.engine.managers.i18n import _t


class Masonry(Tech):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.masonry",
            _t("tech.masonry.name"),
            _t("tech.masonry.description"),
            tech_points_required=20,
            *args,
            **kwargs,
        )
