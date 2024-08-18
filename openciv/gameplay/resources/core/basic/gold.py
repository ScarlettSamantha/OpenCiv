from __future__ import annotations
from openciv.gameplay.resources.core.basic._base import BasicBaseResource
from openciv.engine.managers.i18n import _t


class Gold(BasicBaseResource):
    def __init__(self, value, *args, **kwargs):
        super().__init__(
            "core.basic.gold",
            _t("content.resources.gold.name"),
            _t("content.resources.gold.description"),
            value,
            *args,
            **kwargs,
        )
