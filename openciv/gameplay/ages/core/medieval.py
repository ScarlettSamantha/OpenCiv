from __future__ import annotations
from openciv.gameplay.age import Age
from openciv.engine.managers.i18n import _t


class Medieval(Age):
    def __init__(self, *args, **kwargs):
        super().__init__(
            key="ancient",
            name=_t("content.ages.core.medieval.name"),
            description=_t("content.ages.core.medieval.description"),
            color=(0, 255, 0, 0),
            *args,
            **kwargs,
        )
