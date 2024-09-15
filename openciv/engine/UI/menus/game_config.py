from __future__ import annotations
from openciv.engine.UI.menu import Menu


class GameConfig(Menu):
    """
    TODO this will probably be a different kind of menu, or at least heavily customized...
    either a tabbed_menu, or a "staged" tab menu?
    """
    def __init__(self, game_manager, *args, **kwargs):
        # self.panel = None
        super().__init__(parent=game_manager, *args, **kwargs)

    def setup_content(self):
        return [
            self.Text("<pre>Configure your game</pre>", size=0.012),
            self.ListView(
                ["Small", "Medium", "Large", "Huge"],
                parent=self.parent(),
                title="World Size",
                on_change=lambda x: print(x),  # noqa
            ),
            self.ListView(
                ["Romans", "Egypt", "Large", "Huge"],
                position=(-0.5, 0),
                parent=self.parent(),
                title="Empire",
                on_change=lambda x: print(x),  # noqa
            ),
            self.BackButton()
        ]
