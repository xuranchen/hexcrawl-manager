from hexagon import Hexagon
from biome import Biome

class Map:
    layout = []
    def __init__(self, layout = None):
        self.layout = layout

    def loadMap(self, mapFile):
        mapF = open(mapFile, "r")
        mLayout = []
        for i, x in enumerate(mapF.readlines()):
            mLayout.append([])
            for j, y in enumerate(x.split(" ")):
                mLayout[i].append(Hexagon(i, j, y))
        self.layout = mLayout

if __name__ == '__main__':
    m = Map()
    m.loadMap('test/sample.mp')
    print(m.layout)