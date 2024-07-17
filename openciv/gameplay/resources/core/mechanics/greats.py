from openciv.gameplay.resources.core.mechanics._base import MechanicBaseResource
from openciv.engine.managers.i18n import _t
from typing import Union


class GreatScientist(MechanicBaseResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.great_person_science",
            _t("content.resources.great_person_science.name"),
            _t("content.resources.great_person_science.description"),
            value,
            *args,
            **kwargs,
        )


class GreatArtist(MechanicBaseResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.great_person_culture",
            _t("content.resources.great_person_culture.name"),
            _t("content.resources.great_person_culture.description"),
            value,
            *args,
            **kwargs,
        )


class GreatHero(MechanicBaseResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.great_person_hero",
            _t("content.resources.great_person_hero.name"),
            _t("content.resources.great_person_hero.description"),
            value,
            *args,
            **kwargs,
        )


class GreatHoly(MechanicBaseResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.great_person_faith",
            _t("content.resources.great_person_faith.name"),
            _t("content.resources.great_person_faith.description"),
            value,
            *args,
            **kwargs,
        )


class GreatMilitary(MechanicBaseResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.great_person_military",
            _t("content.resources.great_person_military.name"),
            _t("content.resources.great_person_military.description"),
            value,
            *args,
            **kwargs,
        )


class GreatEngineer(MechanicBaseResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.great_person_engineer",
            _t("content.resources.great_person_engineer.name"),
            _t("content.resources.great_person_engineer.description"),
            value,
            *args,
            **kwargs,
        )


class GreatCommerece(MechanicBaseResource):
    def __init__(self, value: Union[float | int], *args, **kwargs):
        super().__init__(
            "core.mechanic.great_person_commerece",
            _t("content.resources.contentment.name"),
            _t("content.resources.contentment.description"),
            value,
            *args,
            **kwargs,
        )
