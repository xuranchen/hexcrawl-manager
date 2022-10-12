from math import sqrt
from math import cos, sin
import pygame

SQRT3 = sqrt(3)
PI2 = 6.18


class Hexagon:
    def __init__(self, row, col, biome, color):
        self.row = row
        self.col = col
        self.biome = biome
        self.color = color

    # size: size of a single length of the histogram
    def draw(self, radius, surface):
        rowVal = self.row * SQRT3 * radius + SQRT3 * radius
        if self.col %2 == 0:
            rowVal -= SQRT3 * radius / 2
        position = (self.col * radius * 2 + radius - radius / 2 * self.col, rowVal)

        pygame.draw.polygon(surface,
            self.color,
            [(cos(i / 6 * PI2) * radius + position[0], sin(i / 6 * PI2) * radius + position[1]) for i in range(0, 6)])

        pygame.draw.lines(surface,
            (0, 0, 0),
            True,
            [(cos(i / 6 * PI2) * radius + position[0], sin(i / 6 * PI2) * radius + position[1]) for i in range(0, 6)])    


