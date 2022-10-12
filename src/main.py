import pygame
from math import cos, sin, pi
from map import Map


def draw_ngon(Surface, color, n, radius, position):
    pi2 = 2 * pi

    return pygame.draw.polygon(Surface,
        color,
        [(cos(i / n * pi2) * radius + position[0], sin(i / n * pi2) * radius + position[1]) for i in range(0, n)])

pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('main')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False

x =  (display_width * 0.45)
y = (display_height * 0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill((220,220,220))
    #obj = draw_ngon(gameDisplay, (0, 0, 0), 6, 100, (300, 300))
    #pygame.draw.rect(gameDisplay, (0, 0, 0), obj)
    m = Map()
    m.loadMap('test/sample.mp')
    m.drawMap(gameDisplay)


        
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()