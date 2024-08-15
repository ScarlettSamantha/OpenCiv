from __future__ import annotations

from openciv.engine.managers.i18n import T_TranslationOrStr
from openciv.engine.saving import SaveAble
from openciv.gameplay.effect import Effects
from openciv.gameplay.combat.stats import Stats
from openciv.engine.requires import Requires
from typing import Iterator, List, Any


class Item(SaveAble):
    def __init__(
        self,
        key: str,
        name: T_TranslationOrStr,
        description: T_TranslationOrStr,
        icon: str,
        effects: Effects = Effects(),
        requires: Requires = Requires(),
        *args: Any,
        **kwargs: Any,
    ):
        self.key: str = key
        self.name: T_TranslationOrStr = name
        self.description: T_TranslationOrStr = description
        self.icon: str = icon

        self.active: bool = False

        self.effects: Effects = effects
        self.requires: Requires = requires
        self.combat_stats: Stats = Stats()

        self._setup_saveable()


class Items(SaveAble):
    def __init__(
        self,
        key: str | None = None,
        name: T_TranslationOrStr | None = None,
        description: T_TranslationOrStr | None = None,
        icon: str | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        SaveAble.__init__(self, *args, **kwargs)
        self.key: str | None = key
        self.name: T_TranslationOrStr | None = name
        self.description: T_TranslationOrStr | None = description
        self.icon: str | None = icon

        self.items: List[Item] = []
        self._setup_saveable()

    def add_item(self, item: Item) -> Items:
        self.items.append(item)
        return self

    def remove_item(self, item: Item) -> Items:
        self.items.remove(item)
        return self

    def __add__(self, b: Items | Item) -> Items:
        # Add item to items
        if isinstance(b, Item):
            self.items.append(b)
        # Merge items
        elif isinstance(b, Items):  # type: ignore
            self.items.extend(b.items)
        return self

    def __radd__(self, b: Items | Item) -> Items:
        return self.__add__(b)

    def __sub__(self, b: Items | Item) -> Items:
        # Remove item from items
        if isinstance(b, Item):
            self.items.remove(b)
        # Remove all items from items
        elif isinstance(b, Items):  # type: ignore
            for item in b.items:
                self.items.remove(item)
        return self

    def __rsub__(self, b: Items | Item) -> Items:
        return self.__sub__(b)

    def __getitem__(self, key: int) -> Item:
        return self.items[key]

    def __setitem__(self, index: int, value: Item) -> None:
        self.items[index] = value

    def __delitem__(self, index: int) -> None:
        del self.items[index]

    def __iter__(self) -> Iterator[Item]:
        return iter(self.items)

    def __len__(self) -> int:
        return len(self.items)
