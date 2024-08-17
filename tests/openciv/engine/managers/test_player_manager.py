from openciv.engine.managers.player import PlayerManager
from openciv.gameplay.player import Player
from openciv.gameplay.personality import Personality
from openciv.gameplay.civilization import Civilization
from openciv.gameplay.civilizations.rome import Rome
from openciv.gameplay.leaders.alexander import Alexander
from typing import Type
from openciv.ai.ai import AI


import pytest


class TestPlayerManager:
    def _default_civ(self) -> Type[Civilization]:
        return Civilization

    def test_default_state(self) -> None:
        PlayerManager.reset()
        assert PlayerManager.players() == {}
        assert PlayerManager.session_player() is None

    def test_player_add(self) -> None:
        PlayerManager.reset()
        player = Player(
            name="test", turn_order=0, ai=AI(), personality=Personality(), civilization=Rome(), leader=Alexander()
        )
        PlayerManager.add(player, is_session=False)
        assert player == PlayerManager.players()[0]

    def test_player_add_session(self) -> None:
        PlayerManager.reset()
        player = Player(
            name="test", turn_order=0, ai=AI(), personality=Personality(), civilization=Rome(), leader=Alexander()
        )
        PlayerManager.add(player, is_session=True)
        assert player == PlayerManager.player()

    def test_player_get(self) -> None:
        PlayerManager.reset()
        player = Player(
            name="test", turn_order=0, ai=AI(), personality=Personality(), civilization=Rome(), leader=Alexander()
        )
        player2 = Player(
            name="test2", turn_order=1, ai=AI(), personality=Personality(), civilization=Rome(), leader=Alexander()
        )
        PlayerManager.add(player=player)
        assert player == PlayerManager.get(turn=0)
        PlayerManager.add(player=player2)
        assert player2 == PlayerManager.get(turn=1)

    def test_invalid_pregame_condition(self) -> None:
        PlayerManager.reset()
        with pytest.raises(expected_exception=Exception):
            PlayerManager.player()

    def test_turn_exists(self) -> None:
        PlayerManager.reset()
        player = Player(
            name="test", turn_order=0, ai=AI(), personality=Personality(), civilization=Rome(), leader=Alexander()
        )
        PlayerManager.add(player=player)
        assert PlayerManager.turn_exists(turn=0) is True
        assert PlayerManager.turn_exists(turn=1) is False
