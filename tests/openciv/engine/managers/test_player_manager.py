from openciv.engine.managers.player import PlayerManager
from openciv.gameplay.player import Player
from openciv.gameplay.personality import Personality
from openciv.gameplay.civilization import Civilization
from openciv.gameplay.civilizations.rome import Rome
from openciv.gameplay.leader import Leader

from openciv.ai.ai import AI


import pytest


class TestPlayerManager:
    def _default_civ():
        return Civilization

    def test_default_state(self):
        PlayerManager.reset()
        assert PlayerManager._players == {}
        assert PlayerManager._session_player is None

    def test_player_add(self):
        PlayerManager.reset()
        player = Player(
            name="test", turn_order=0, ai=AI(), personality=Personality(), civilization=Rome(), leader=Leader()
        )
        PlayerManager.add(player, is_session=False)
        assert player == PlayerManager._players[0]

    def test_player_add_session(self):
        PlayerManager.reset()
        player = Player(
            name="test", turn_order=0, ai=AI(), personality=Personality(), civilization=Rome(), leader=Leader()
        )
        PlayerManager.add(player, is_session=True)
        assert player == PlayerManager.player()

    def test_player_get(self):
        PlayerManager.reset()
        player = Player(
            name="test", turn_order=0, ai=AI(), personality=Personality(), civilization=Rome(), leader=Leader()
        )
        player2 = Player(
            name="test2", turn_order=1, ai=AI(), personality=Personality(), civilization=Rome(), leader=Leader()
        )
        PlayerManager.add(player)
        assert player == PlayerManager.get(0)
        PlayerManager.add(player2)
        assert player2 == PlayerManager.get(1)

    def test_invalid_pregame_condition(self):
        PlayerManager.reset()
        with pytest.raises(Exception):
            PlayerManager.player()

    def test_turn_exists(self):
        PlayerManager.reset()
        player = Player(
            name="test", turn_order=0, ai=AI(), personality=Personality(), civilization=Rome(), leader=Leader()
        )
        PlayerManager.add(player)
        assert PlayerManager.turn_exists(0) is True
        assert PlayerManager.turn_exists(1) is False
