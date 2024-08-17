from openciv.engine.managers.base import BaseManager
from openciv.gameplay.player import Player

from typing import Dict

from openciv.engine.exceptions.invalid_pregame_condition import InvalidPregameCondition


class PlayerManager(BaseManager):
    _players: Dict[
        int, Player
    ] = {}  # Players are stored in a dictionary with the key being the turn order. recalculated each turn.
    _session_player: Player | None = None

    @classmethod
    def reset(cls) -> None:
        cls._players = {}
        cls._session_player = None

    @classmethod
    def add(cls, player: Player, is_session: bool = False) -> None:
        if cls.turn_exists(player.turn_order):
            raise InvalidPregameCondition(f"Player with turn order {player.turn_order} already exists.")
        cls._players[player.turn_order] = player
        if is_session:
            cls._session_player = player

    @classmethod
    def turn_exists(cls, turn: int) -> bool:
        for _, obj in cls._players.items():
            if obj.turn_order == turn:
                return True
        return False

    @classmethod
    def get(cls, turn: int) -> Player:
        print(cls._players)
        return cls._players[turn]

    @classmethod
    def players(cls) -> Dict[int, Player]:
        return cls._players

    @classmethod
    def player(cls) -> Player:
        if cls._session_player is None:
            raise InvalidPregameCondition("No player has been set for this session.")
        return cls._session_player
