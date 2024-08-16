from openciv.engine.UI.menus.base import Menu


class MainMenu(Menu):
    def __init__(self, game_manager, call: callable):
        Menu.__init__(parent=game_manager, onstart=call, title='OpenCiv', popup=False)

    def set_menu_content(self):
        into_text = self.Text("<pre>A game in very early development/protyping just a fun exercise\n</pre>", size=0.012)
        footer_text = self.Text("By: Scarlett Samantha Verheul <scarlett.verheul@gmail.com>", size=0.012)

        self.content = [
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

    
