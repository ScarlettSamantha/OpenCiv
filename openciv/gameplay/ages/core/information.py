from __future__ import annotations
from openciv.gameplay.age import Age
from openciv.engine.managers.i18n import _t


class Information(Age):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="ancient",
            name=_t("content.ages.core.information.name"),
            description=_t("content.ages.core.information.description"),
            color=(0, 255, 0, 0),
            *args,
            **kwargs,
        )
