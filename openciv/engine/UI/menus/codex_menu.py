from openciv.engine.UI.menu import Menu

class CodexMenu(Menu):
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, title='Codex', popup=False, *args, **kwargs)

    def setup_content(self):
        return [
            self.Text('Codex of in game info like empires, techs, cultures, units, etc.', size=0.012),
            self.Text('Perhaps also even in-game stats?'),
            self.BackButton()
        ]

