from enum import Enum

FOREST = "FOREST"
PLAINS = "PLAINS"
MOUNTAIN = "MOUNTAIN"
SWAMP = "SWAMP"
ISLAND = "ISLAND"
class Biome():

    
    def get(biomeStr):
        if biomeStr == FOREST:
            return(Forest())
        elif biomeStr == PLAINS:
            return(Plains())
        elif biomeStr == MOUNTAIN:
            return(Mountain())
        elif biomeStr == ISLAND:
            return(Island())
        elif biomeStr == SWAMP:
            return(Swamp())
        else:
            print("the fuck is " + biomeStr)

class Forest(Biome):
    def getColor(self):
        return((0, 255, 0))

class Swamp(Biome):
    def getColor(self):
        return((0, 0, 0))

class Island(Biome):
    def getColor(self):
        return((0, 0, 255))

class Plains(Biome):
    def getColor(self):
        return((255, 255, 255))

class Mountain(Biome):
    def getColor(self):
        return((255, 0, 0))