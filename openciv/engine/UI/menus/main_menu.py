from typing import Any
from openciv.engine.UI.menu import Menu
from openciv.engine.UI.menus.options_menu import OptionsMenu
from openciv.engine.UI.menus.mods_menu import ModsMenu
from openciv.engine.UI.menus.test_menu import TestMenu
from openciv.engine.UI.menus.game_config import GameConfig
from openciv.engine.UI.menus.saves_menu import SavesMenu
from openciv.engine.UI.menus.codex_menu import CodexMenu


class MainMenu(Menu):
    def __init__(self, game_manager):
        super().__init__(parent=game_manager, title='OpenCiv', popup=False)

    def setup_content(self) -> "list[Any]":
        intro_text = self.Text("<pre>A game in very early development/protyping just a fun exercise\n</pre>", size=0.012)
        footer_text = self.Text("By: Scarlett Samantha Verheul <scarlett.verheul@gmail.com>", size=0.012)

        return [
            intro_text,
            self.NavButton(text="New Game", destination=GameConfig),
            self.NavButton(text="Resume", destination=SavesMenu),
            self.NavButton(text="Options", destination=OptionsMenu),
            self.NavButton(text="Codex", destination=CodexMenu),
            self.NavButton(text="Mods", destination=ModsMenu),
            self.LinkButton(text="Wiki", url='https://github.com/ScarlettSamantha/openciv-meta'),
            self.LinkButton(text="Source", url='https://github.com/ScarlettSamantha/OpenCiv'),
            # self.NavButton(text="Dev", destination=TestMenu),
            self.Button(text="Exit", click_action=self.parent().shutdown),
            footer_text,
        ]
    
