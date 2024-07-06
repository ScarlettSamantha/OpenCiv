from ursina import WindowPanel, Text
from openciv.world.tiles._base_tile import BaseTile

class UI():

    def __init__(self):
        pass

    def mainWindow(self, tile):
        TileInstance: BaseTile = tile.tile

        content = [
            Text("Terrain: {}".format(tile.tile.terrain.name)),
            Text("X: {}, Y:{}".format(tile._x, tile._y))
        ]

        t = ""
        for modifier in TileInstance.terrain.get_modifiers()._modifiers:
            t += "Modifier: {} | {}".format(modifier._property, modifier._value) + "\n"

        content.append(Text(t))


        self.panel = WindowPanel(title='Custom Window', content=content,popup=True)
        self.panel.y = self.panel.scale_y / 2 * self.panel.scale_y    # center the window panel
        self.panel.enabled = True
        self.panel.layout()
