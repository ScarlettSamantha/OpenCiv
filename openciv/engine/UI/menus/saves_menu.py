from openciv.engine.UI.menu import Menu

class SavesMenu(Menu):
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, title='Saved Games', popup=False, *args, **kwargs)

    def setup_content(self):
        return [
            self.Text('Menu where player can resume, delete, or otherwise manage existing game saves...', size=0.012),
            self.BackButton()
        ]