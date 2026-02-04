import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)

rect(screen, GRAY, (0, 0, 400, 400))
circle(screen, YELLOW, (200, 200), 100)
circle(screen, BLACK, (200, 200), 100, 1)
rect(screen, BLACK, (150, 250, 100, 20))
circle(screen, RED, (150, 180), 25)
circle(screen, BLACK, (150, 180), 25, 1)
circle(screen, BLACK, (150, 180), 10)
circle(screen, RED, (250, 180), 20)
circle(screen, BLACK, (250, 180), 20, 1)
circle(screen, BLACK, (250, 180), 10)
polygon(screen, BLACK, [[180, 175], [185, 165], [120, 110], [115, 120]])
polygon(screen, BLACK, [[230, 175], [225, 165], [280, 110], [285, 120]])



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()