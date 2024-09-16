from openciv.engine.UI.menu import Menu, TabbedMenu, SubMenu


# TODO subclass TabbedMenu instead of Menu when it is implemented
class OptionsMenu(TabbedMenu):
    def __init__(self, game_manager, *args, **kwargs):
        super().__init__(parent=game_manager, title='Game Options', *args, **kwargs)

    class GameOptions(SubMenu):
        def __init__(self, parent_menu: Menu, *args, **kwargs):
            super().__init__(parent_menu, 'Gameplay', *args, **kwargs)

        def setup_content(self):
            return [
                self.Text('Core gameplay settings...')
            ]

    class GraphicsOptions(SubMenu):
        def __init__(self, parent_menu: Menu, *args, **kwargs):
            super().__init__(parent_menu, 'Graphics', *args, **kwargs)

        def setup_content(self):
            return [
                self.Text('Visual settings...')
            ]

    class ControlOptions(SubMenu):
        def __init__(self, parent_menu: Menu, *args, **kwargs):
            super().__init__(parent_menu, 'Controls', *args, **kwargs)

        def setup_content(self):
            return [
                self.Text('Keybindings and other controls...')
            ]

    class AudioOptions(SubMenu):
        def __init__(self, parent_menu: Menu, *args, **kwargs):
            super().__init__(parent_menu, 'Audio', *args, **kwargs)

        def setup_content(self):
            return [
                self.Text('Audio settings...')
            ]

    class AccessibilityOptions(SubMenu):
        def __init__(self, parent_menu: Menu, *args, **kwargs):
            super().__init__(parent_menu, 'Accessibility', *args, **kwargs)

        def setup_content(self):
            return [
                self.Text('Accessibility options...')
            ]

    def get_submenu_tabs(self):
        return (
            self.GameOptions,
            self.ControlOptions,
            self.GraphicsOptions,
            self.AudioOptions,
            self.AccessibilityOptions
        )
    
    def get_submenu_names(self) -> "tuple[str]":
        # TODO: make this dynamic, instead of hardcoding...
        return (
            'Gameplay',
            'Graphics',
            'Controls',
            'Audio',
            'Accessibility'
        )

    def setup_content(self):
        return [
            self.Text("<pre>This tabbed menu will allow player to configure variety of ingame options...</pre>", ),
            self.TabGroup(tabbed_menu=self),
            self.BackButton()
        ]