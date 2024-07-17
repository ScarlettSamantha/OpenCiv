from openciv.gameplay.resources.core.mechanics._base import MechanicBaseResource
from openciv.engine.managers.i18n import _t
from typing import Union


class Contentment(MechanicBaseResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.contentment",
            _t("content.resources.contentment.name"),
            _t("content.resources.contentment.description"),
            value,
            *args,
            **kwargs,
        )
