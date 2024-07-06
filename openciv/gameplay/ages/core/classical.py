from openciv.gameplay.age import Age
from openciv.engine.managers.i18n import _t


class Classical(Age):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "classical",
            _t("content.ages.core.classical.name"),
            _t("content.ages.core.classical.description"),
            color=(255, 0, 0, 0),
            *args,
            **kwargs,
        )
