from openciv.gameplay.resources.core.basic._base import BasicBaseResource
from openciv.engine.managers.i18n import _t


class Faith(BasicBaseResource):
    def __init__(self, value, *args, **kwargs):
        super().__init__(
            "core.basic.faith",
            _t("content.resources.faith.name"),
            _t("content.resources.faith.description"),
            value,
            *args,
            **kwargs,
        )
