from openciv.engine.UI.base import BaseUI


class MainMenu(BaseUI):
    def __init__(self, game_manager, call: callable, *args, **kwargs):
        self.panel = None
        self.on_start: callable = call
        super().__init__(parent=game_manager, *args, **kwargs)

    def render(self):
        into_text = self.Text("<pre>A game in very early development/protyping just a fun exercise\n</pre>", size=0.012)
        footer_text = self.Text("By: Scarlett Samantha Verheul <scarlett.verheul@gmail.com>", size=0.012)

        content = [
            into_text,
            self.Button(text="New Game", click_action=lambda: self.on_start(), radius=0.0),
            self.Button(text="Save", radius=0.0),
            self.Button(text="Load", radius=0.0),
            self.Button(text="Options", radius=0.0),
            self.Button(text="Mods", radius=0.0),
            self.Button(text="Wiki", radius=0.0),
            self.Button(text="Source", radius=0.0),
            self.Button(text="Dev", radius=0.0, click_action=lambda: self.parent().ui().start_test_menu()),
            self.Button(text="Exit", click_action=self.parent().shutdown, radius=0.0),
            footer_text,
        ]
        self.panel = self.WindowPanel(title="Openciv", content=content, popup=False)

        self.center()
        self.panel.enabled = False
        self.panel.layout()
        self.panel.y += 0.4

    def center(self):
        self.panel.y = self.panel.scale_y / 2 * self.panel.scale_y

    def show(self):
        self.panel.enabled = True

    def hide(self):
        self.panel.enabled = False
