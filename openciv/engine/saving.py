from openciv.engine.additions.hex_grid import HexGrid


import pickle

class Saving():


    def __init__(self):
        pass


    def toJson(self, data: HexGrid):
        data = pickle.dumps(data)
        print(str(data).__len__())
