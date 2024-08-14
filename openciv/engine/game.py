from ursina import Entity, Ursina
from pathlib import Path
from random import Random
from dotenv import dotenv_values
from importlib import util

from openciv.engine.managers.config import Config
from openciv.engine.managers.log import LogManager
from openciv.engine.camera import Camera

from openciv.engine.managers.game import GameManager, GameManagerInstance
from openciv.engine.managers.map import MapManager
from openciv.engine.managers.market import MarketManager
from openciv.engine.managers.player import PlayerManager
from openciv.engine.managers.turn import TurnManager
from openciv.engine.managers.knowledge import KnowledgeManager
from openciv.engine.managers.tech import TechManager
from openciv.engine.managers.culture import CultureManager
from openciv.engine.managers.ui import UIManager
from openciv.engine.managers.i18n import _i18n, set_i18n
from openciv.engine.additions.hex_grid import HexGrid


class Game:
    def __init__(
        self,
        width: int = 1920,
        height: int = 1080,
        title: str = "OpenCiv",
        fullscreen: bool = False,
        vsync: bool = False,
        show_fps: bool = True,
        hertz: int = 60,
        display: int = 0,
    ):
        self.width = width
        self.height = height
        self.title = title
        self.fullscreen = fullscreen
        self.vsync = vsync
        self.show_fps = show_fps
        self.hertz = hertz
        self.display = display
        self.env = {}

        self.icon: str = "./openciv/assets/images/game_icon.png"
        self.development_mode = True
        self.render_mode = None
        self.show_splash = False
        self.editor_ui_enabled = False

        self.hex_grid = None

        self.camera = None
        self.game_manager: GameManager = None

        self.ursina: Ursina
        self.setup_dotenv()
        if self.env["sentry_enabled"] and util.find_spec("sentry_sdk"):
            self.setup_sentry()
        self.setup_engine()
        self.setup_camera()
        self.prepare_game_managers()
        self.prepare_map()

    def setup_engine(self) -> None:
        log_manager = LogManager._get_instance()
        log_manager.engine.debug("Setting up engine")
        self.ursina = Ursina(
            title=self.title,
            icon=self.icon,
            fullscreen=self.fullscreen,
            size="",
            vsync=self.vsync,
            editor_ui_enabled=self.editor_ui_enabled,
            window_type="onscreen",
            development_mode=self.development_mode,
            render_mode=self.render_mode,
            show_ursina_splash=self.show_splash,
            borderless=False,
        )
        log_manager.engine.debug("Engine setup complete")

    def setup_dotenv(self) -> None:
        # Nearly identical to calling dotenv.load_dotenv(), except it returns any parsed env vars as a dict
        self.env = dotenv_values()

    def setup_sentry(self) -> None:
        # We have to import sentry here because it's not a dependency
        import sentry_sdk

        sentry_sdk.init(
            dsn=self.env["sentry_license_key"],
            traces_sample_rate=1.0,
            profiles_sample_rate=1.0,
        )

    def setup_camera(self) -> None:
        self.camera = Camera(None)

    def get_base_path(self):
        return Path(__file__).resolve().parent.parent.parent

    def get_path(self, path: Path):
        return Path(self.get_base_path() / path)

    def prepare_game_managers(self) -> None:
        config = Config(self.get_path("config.json"))
        config.load()
        i18n_manager = _i18n(config.get("game.engine.init.i18n.path.relative"), config.get("game.language"), True)
        i18n_manager.load_language("en_EN")
        set_i18n(i18n_manager)
        log_manager = LogManager._get_instance()
        log_manager.engine.debug("Preparing game managers")
        map_manager = MapManager()
        map_manager.load("openciv/world/tiles/")
        log_manager.engine.debug("Map manager created")
        player_manager = PlayerManager()
        log_manager.engine.debug("Player manager created")
        market_manager = MarketManager()
        log_manager.engine.debug("Market manager created")
        turn_manager = TurnManager()
        log_manager.engine.debug("Turn manager created")
        knowledge_manager = KnowledgeManager()
        log_manager.engine.debug("Knowledge manager created")
        tech_manager = TechManager()
        log_manager.engine.debug("Tech manager created")
        culture_manager = CultureManager()
        log_manager.engine.debug("Culture manager created")
        ui_manager = UIManager()
        log_manager.engine.debug("UI manager created")

        name = "Devgame - {}".format(Random().randint(1, 90000))

        self.game_manager = GameManagerInstance(
            name=name,
            i18n_manager=i18n_manager,
            config_manager=config,
            camera=self.camera,
            map_manager=map_manager,
            player_manager=player_manager,
            market_manager=market_manager,
            turn_manager=turn_manager,
            knowledge_manager=knowledge_manager,
            tech_manager=tech_manager,
            culture_manager=culture_manager,
            ui_manager=ui_manager,
            log_manager=log_manager,
        )
        log_manager.engine.debug("Game managers prepared")

        self.camera.game_manager = self.game_manager

    def prepare_map(self) -> None:
        log_manager = LogManager._get_instance()
        log_manager.engine.debug("Preparing map")
        hexGridEntity = HexGrid(16, 16, tiles=self.game_manager.map().registeredTiles())
        log_manager.engine.debug("Hex grid entity created")
        self.hex_grid = hexGridEntity
        grid_Entity = Entity(model=hexGridEntity, scale=1, rotation_x=90, y=1)
        self.camera.grid_ref = self.hex_grid
        self.game_manager.map().setDataRaw(self.hex_grid)
        log_manager.engine.debug("Map prepared")

    def run(self):
        self.game_manager.boot()
        log_manager = LogManager._get_instance()
        log_manager.engine.debug("Game booted")
        log_manager.gameplay.debug("Game starting")
        self.game_manager.run()
        self.game_manager.ui().start_main_menu()
        self.game_manager.camera().gameInteractive(False)
        self.ursina.run()
