from hexagon import Hexagon
from biomes.biome import Biome

class Map:
    layout = []
    def __init__(self, layout = None):
        self.layout = layout

    def loadMap(self, mapFile):
        with open(mapFile) as f:
            fileList = f.read().splitlines() 
            mLayout = []
            for i, x in enumerate(fileList):
                mLayout.append([])
                for j, y in enumerate(x.split(" ")):
                    biome = Biome.get(y)
                    mLayout[i].append(Hexagon(i, j, biome, biome.getColor()))
            self.layout = mLayout

    def drawMap(self, surface):
        for i, x in enumerate(self.layout):
            for j, hex in enumerate(x):
                hex.draw(50, surface)

if __name__ == '__main__':
    m = Map()
    m.loadMap('test/sample.mp')
    print(m.layout)