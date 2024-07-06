from openciv.gameplay.age import Age
from openciv.engine.managers.i18n import _t


class Renaissance(Age):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="ancient",
            name=_t("content.ages.core.renaissance.name"),
            description=_t("content.ages.core.renaissance.description"),
            color=(0, 255, 0, 0),
            *args,
            **kwargs,
        )
