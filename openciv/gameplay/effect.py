from __future__ import annotations

from openciv.engine.managers.i18n import T_TranslationOrStr
from openciv.engine.saving import SaveAble
from openciv.engine.requires import Requires
from openciv.gameplay.resource import Resource
from openciv.gameplay.planes.plane import Plane
from openciv.gameplay.combat.stats import Stats
from openciv.engine.exceptions.effects_exception import EffectCannotBeBoughtOff, EffectDoesNotExist
from openciv.engine.managers.log import LogManager

from typing import Type, List, Dict, Union, Any, Generator


class Targetable:
    def __init__(self) -> None:
        self.targetable = True


class EffectTargetType(SaveAble):
    def __init__(self, key: str, target_planes: Plane, *args: Any, **kwargs: Any) -> None:
        SaveAble.__init__(self=self, *args, **kwargs)
        self.key: str = key
        self.target_planes: Plane = target_planes

        self._setup_saveable()


class EffectTargetTypeTile(EffectTargetType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="system.effect_target_type.tile", *args, **kwargs)


class EffectTargetTypeCity(EffectTargetType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="system.effect_target_type.city", *args, **kwargs)


class EffectTargetTypeProvince(EffectTargetType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="system.effect_target_type.province", *args, **kwargs)


class EffectTargetTypePlayer(EffectTargetType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="system.effect_target_type.player", *args, **kwargs)


class EffectTargetTypeGlobal(EffectTargetType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="system.effect_target_type.global", *args, **kwargs)


class EffectTargetTypeRadius(EffectTargetType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="system.effect_target_type.radius", *args, **kwargs)


class EffectTargetTypeFixed(EffectTargetType):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(key="system.effect_target_type.fixed", *args, **kwargs)


T_EffectTarget = Union[
    EffectTargetTypeCity,
    EffectTargetTypeTile,
    EffectTargetTypeProvince,
    EffectTargetTypePlayer,
    EffectTargetTypeGlobal,
    EffectTargetTypeRadius,
    EffectTargetTypeFixed,
]

T_EffectTargetType = Type[T_EffectTarget]


class Effect(SaveAble):
    def __init__(
        self,
        key: str,
        name: T_TranslationOrStr,
        description: T_TranslationOrStr,
        icon: str | None = None,
        target: Targetable | None = None,
        target_type: Type[EffectTargetType] | None = None,
        active: bool = True,
        requires: Requires | None = None,
        can_player_self_deactivate: bool = False,
        can_player_self_activate: bool = False,
        can_buyoff: bool = False,
        buyoff_cost: int = 0,
        buyoff_resource: Type[Resource] | None = None,
        combat_stats: Stats = Stats(),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        SaveAble.__init__(self=self, *args, **kwargs)
        self.key: str = key
        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr = description
        self.icon: str | None = icon
        self.active: bool = active

        self._target: Targetable | None = target
        self.target_type: Type[EffectTargetType] | None = target_type
        self.is_bought_off: bool = False

        self.buyoff_cost: int = buyoff_cost
        self.buyoff_resource: Type[Resource] | None = buyoff_resource
        self.can_buyoff: bool = can_buyoff
        self.can_player_self_activate: bool = can_player_self_activate
        self.can_player_self_deactivate: bool = can_player_self_deactivate

        self.requires: Requires | None = requires

        self.combat_stats: Stats = combat_stats

        self._mechanics: List[Any] = []
        self._links: List[Any] = []
        self._tags: List[Any] = []

        self._setup_saveable()

    def buyoff(self, change_active: bool = True, fail_on_unallowed_buyoff: bool = True) -> Effect:
        if not self.can_buyoff:
            if fail_on_unallowed_buyoff:
                raise EffectCannotBeBoughtOff(f"Effect {self.key} cannot be bought off")
            return self
        self.is_bought_off = True
        self.active = False if change_active else self.active
        return self

    @property
    def target(self) -> Targetable | None:
        return self._target

    @target.setter
    def target(self, target: Targetable) -> None:
        self._target = target


class Effects(SaveAble):
    def __init__(self, name: T_TranslationOrStr | None = None, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.index: int = 0
        self.effects: Dict[str, Effect] = {}
        self.name: T_TranslationOrStr | None = name
        self._setup_saveable()
        # We need to calculate the effects of all effects in the here to be able to give combat_stats.
        self.combat_stats: Stats = Stats()

        # We don't want this to be saved.
        self.logger: LogManager = LogManager.get_instance()

    def add(self, effect: Effect, key_or_auto: str | None = None, auto_add_name_on_empty: bool = True) -> None:
        if auto_add_name_on_empty and getattr(effect, "name") is None:
            effect.name = f"!nameless_effect_from_{self.name}_{self.index}"
        self.logger.loggers["gameplay"].debug(f"Adding effect {effect.name} to {self.name}")
        self.effects[effect.key if key_or_auto is None else key_or_auto] = effect
        self.index += 1

    def get(self, key: str, fail_on_not_found: bool = True) -> Effect | None:
        if key not in self.effects:
            if fail_on_not_found:
                raise EffectDoesNotExist(f"Effect {key} does not exist in {self.name}")
            self.logger.loggers["gameplay"].debug(
                msg=f"[FIX]: Effect {key} is attempted to be retrieved but does not exist in {self.name}"
            )
            return None
        return self.effects[key]

    def has(self, key: str) -> bool:
        return key in self.effects

    def delete(self, key: str, fail_on_not_found: bool = True) -> None:
        if key not in self.effects:
            if fail_on_not_found:
                raise EffectDoesNotExist(f"Effect {key} does not exist in {self.name}")
            return
        self.logger.loggers["gameplay"].debug(f"Deleting effect {self.effects[key].name} from {self.name}")
        del self.effects[key]

    def __iter__(self) -> Generator[Effect, None, None]:
        for effect in self.effects.values():
            yield effect

    def __setitem__(self, key: str, effect: Effect) -> None:
        self.add(effect=effect)

    def __getitem__(self, key: str) -> Effect | None:
        return self.get(key=key)

    def __delitem__(self, key: str) -> None:
        self.delete(key=key)

    def _merge_effects(self, effects: List[Effect]) -> Effects:
        new_effects = Effects(name=self.name)
        for effect in self:
            new_effects.add(effect=effect)
        for effect in effects:
            new_effects.add(effect=effect)
        return new_effects

    def _merge_effects_dict(self, effects: Dict[str, Effect]) -> Effects:
        new_effects = Effects(name=self.name)
        for effect in self:
            new_effects.add(effect=effect)
        for effect in effects.values():
            new_effects.add(effect=effect)
        return new_effects

    def __add__(self, other: Effects | List[Effect] | Dict[str, Effect]) -> Effects:
        if isinstance(other, (Effects, list)):
            return self._merge_effects(effects=list(other))
        elif isinstance(other, dict):  # type: ignore
            return self._merge_effects_dict(effects=other)
        else:
            raise TypeError("Can only merge with another Effects instance, list of Effects, or dict of Effects")

    def __radd__(self, other: Effects | List[Effect] | Dict[str, Effect]) -> Effects:
        return self.__add__(other)

    def __sub__(self, other: Effects | str | List[str]) -> Effects:
        new_effects = Effects(name=self.name)
        for effect in self:
            new_effects.add(effect=effect)
        if isinstance(other, Effects):
            for effect in other:
                new_effects.delete(effect.key, fail_on_not_found=False)
        elif isinstance(other, str):
            new_effects.delete(other, fail_on_not_found=False)
        elif isinstance(other, list):  # type: ignore
            for key in other:
                new_effects.delete(key=key, fail_on_not_found=False)
        else:
            raise TypeError("Can only subtract with another Effects instance, str, or list of str")
        return new_effects

    def __rsub__(self, other: Effects) -> Effects:
        return other.__sub__(other=self)

    def __len__(self) -> int:
        return len(self.effects)
