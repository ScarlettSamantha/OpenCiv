from openciv.gameplay.resources.core.mechanics._base import MechanicBaseResource
from openciv.engine.managers.i18n import _t
from typing import Union


class Stability(MechanicBaseResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.stability",
            _t("content.resources.stability.name"),
            _t("content.resources.stability.description"),
            value,
            *args,
            **kwargs,
        )
