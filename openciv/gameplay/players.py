from __future__ import annotations
from openciv.gameplay.player import Player
from typing import Type


class Players:
    def __init__(self):
        self._data = {}

    def addPlayer(self, player: Player):
        self._data[player.turn_order] = player
        self.reorderTurnOrder()

    def removePlayer(self, player: Player):
        del self._data[player.turn_order]
        self.reorderTurnOrder()

    def __getitem__(self, _, key):
        return self._data[key]

    def __delitem__(self, _, key: Type[int | Player]):
        if isinstance(key, int):
            self.removePlayer(key)
        elif isinstance(key, Player):
            self.removePlayer(key.turn_order)

    def reorderTurnOrder(self):
        sorted_items = sorted(self._data.items(), key=lambda item: item.turn_order)
        self._data = dict(sorted_items)
