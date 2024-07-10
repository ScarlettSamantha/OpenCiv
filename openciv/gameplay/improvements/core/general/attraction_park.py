from openciv.gameplay.improvement import Improvement
from openciv.gameplay.tile_yield import TileYield
from openciv.engine.managers.tags import Tag
from openciv.engine.managers.i18n import _t


class AttractionPark(Improvement):
    def __init__(self, *args, **kwargs):
        super().__init__(
            "core.improvement.general.attraction_park",
            _t("content.improvements.core.general.attraction_park.name"),
            _t("content.improvements.core.general.attraction_park.description"),
            *args,
            **kwargs,
        )

        self.health = 50
        self.max_health = 50

        self.tile_yield_improvement = TileYield(name="military_base", food=1.0, mode=TileYield.ADDITIVE)

        self.add_tag(Tag("builder", self))
