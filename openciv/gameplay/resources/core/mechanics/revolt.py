from __future__ import annotations
from openciv.gameplay.resources.core.mechanics._base import MechanicBaseResource
from openciv.engine.managers.i18n import _t
from typing import Union


class Revolt(MechanicBaseResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.revolt",
            _t("content.resources.revolt.name"),
            _t("content.resources.revolt.description"),
            value,
            *args,
            **kwargs,
        )
