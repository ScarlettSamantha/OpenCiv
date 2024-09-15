from openciv.engine.UI.menu import Menu

class ModsMenu(Menu):
    def __init__(self, parent):
        super().__init__(parent, 'OpenCiv Mods', popup=False)

    def setup_content(self):
        return [
            self.Text('Screen where any installed mods are listed & managed...', size=0.012),
            self.BackButton()
        ]