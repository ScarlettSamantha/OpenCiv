from openciv.engine.managers.base import BaseManager

from openciv.engine.managers.map import MapManager
from openciv.engine.managers.market import MarketManager
from openciv.engine.managers.player import PlayerManager
from openciv.engine.managers.turn import TurnManager

from openciv.engine.managers.knowledge import KnowledgeManager
from openciv.engine.managers.tech import TechManager
from openciv.engine.managers.culture import CultureManager
from openciv.engine.managers.ui import UIManager
from openciv.engine.managers.i18n import i18n
from openciv.engine.managers.config import Config
from openciv.engine.managers.log import LogManager
from openciv.gameplay.civilizations.rome import Rome
from openciv.gameplay.leaders.ceasar import Ceasar
from openciv.gameplay.player import Player
from openciv.gameplay.resource import ResourceValueType
from typing import Union, List

GameManagerInstance = None


class GameManager(BaseManager):
    def __init__(self):
        pass

    def __setup__(
        self,
        name,
        camera: "Camera",  # noqa: F821
        log_manager: LogManager,
        i18n_manager: i18n,
        config_manager: Config,
        map_manager: MapManager,
        player_manager: PlayerManager,
        market_manager: MarketManager,
        turn_manager: TurnManager,
        knowledge_manager: KnowledgeManager,
        tech_manager: TechManager,
        culture_manager: CultureManager,
        ui_manager: UIManager,
    ):
        self.name = name

        self.i18n_manager: i18n = i18n_manager
        self.config_manager: Config = config_manager
        self.map_manager: MapManager = map_manager
        self.player_manager: PlayerManager = player_manager
        self.market_manager: MarketManager = market_manager
        self.turn_manager: TurnManager = turn_manager
        self.knowledge_manager: KnowledgeManager = knowledge_manager
        self.tech_manager: TechManager = tech_manager
        self.culture_manager: CultureManager = culture_manager
        self.ui_manager: UIManager = ui_manager
        self.log_manager: LogManager = log_manager
        self._camera: "Camera" = camera  # noqa: F821

    def configure_managers(self):
        def give_managers_parents(self):
            self.map_manager.setParent(self)
            self.market_manager.setParent(self)
            self.player_manager.setParent(self)
            self.turn_manager.setParent(self)

            self.knowledge_manager.setParent(self)
            self.tech_manager.setParent(self)
            self.culture_manager.setParent(self)
            self.ui_manager.setParent(self)

        give_managers_parents(self)

    def boot(self):
        self.configure_managers()

    def run(self):
        window = self.ui().start_main_menu()

    def configure_game(self):
        pass

    def start_game(self):
        def load_resources(self):
            from openciv.engine.additions.pyload import PyLoad

            resources = PyLoad.load_classes("openciv/gameplay/resources/")
            resource_list = []
            for _, resource in resources.items():
                resource_list.append(resource)

        def init_player(self, resources: Union[List | "Resource"] = None):  # noqa: F821
            leader = Ceasar()
            civilization = Rome()
            player = Player(
                name="Dev Player",
                turn_order=0,
                ai=False,
                personality=None,
                civilization=civilization,
                leader=leader,
            )

            if resources is not None:
                for resource in resources:
                    resource.value = 0 if resource._value_storage == ResourceValueType.INT else 0.0
                    player.resources.add(resource)

            self.player().add(player, is_session=True)

        def init_board(self):
            self.map().generate()

        def place_player(self):
            self.map().place_player()

        def check_state(self):
            self.map().check_state()

        def setup_turns(self):
            self.turn().setup()

        def finish(self):
            self.ui().start_game()

        resources = load_resources(self)
        init_player(self, resources)
        init_board(self)
        place_player(self)
        check_state(self)
        setup_turns(self)
        finish(self)

    def map(self) -> MapManager:
        return self.map_manager

    def player(self) -> PlayerManager:
        return self.player_manager

    def market(self) -> MarketManager:
        return self.market_manager

    def turn(self) -> TurnManager:
        return self.turn_manager

    def knowledge(self) -> KnowledgeManager:
        return self.knowledge_manager

    def tech(self) -> TechManager:
        return self.tech_manager

    def culture(self) -> CultureManager:
        return self.culture_manager

    def ui(self) -> UIManager:
        return self.ui_manager

    def config(self) -> Config:
        return self.config_manager

    def camera(self) -> "Camera":  # noqa: F821
        return self._camera

    def log(self) -> LogManager:
        return LogManager._get_instance()

    def shutdown(self):
        print("Shutdown")
        exit(0)

    def __call__(self, *args, **kwargs):
        self.__setup__(**kwargs)
        return self


if GameManagerInstance is None:
    GameManagerInstance = GameManager()
