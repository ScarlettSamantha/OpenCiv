from openciv.gameplay.age import Age
from openciv.engine.managers.i18n import _t


class Modern(Age):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="ancient",
            name=_t("content.ages.core.modern.name"),
            description=_t("content.ages.core.modern.description"),
            color=(0, 255, 0, 0),
            *args,
            **kwargs,
        )
