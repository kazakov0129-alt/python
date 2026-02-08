import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500,400))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (170, 255, 255)
SEA_BLUE = (100, 50, 255)
YELLOW = (255, 255, 0)
BROWN = (255, 120, 60)
RED_BROWN = (255, 90, 60)
BEIGE = (245, 245, 220)


rect(screen, BLUE, (0, 0, 500, 150))         # sky
rect(screen, SEA_BLUE, (0, 150, 500, 100))   # sea
rect(screen, YELLOW, (0, 250, 500, 150))     # sand
circle(screen, YELLOW, (450, 50), 40)        # sun
x = 105
for i in range(3):
	circle(screen, WHITE, (x, 40), 20)
	circle(screen, BLACK, (x, 40), 20, 1)
	x += 30                                   #cloud
x = 95
for i in range(4):
	circle(screen, WHITE, (x, 60), 20)
	circle(screen, BLACK, (x, 60), 20, 1)
	x += 30
rect(screen, BROWN, (90, 220, 10, 150))       #branch
#roof
polygon(screen, RED_BROWN, [[35, 220], [155, 220], [100, 190], [90, 190]]) #roof
x = 35
for i in range(4):
	line(screen, BLACK, [90, 190], [x, 220], 1)
	x += 55 / 3
x = 100
for i in range(4):
	line(screen, BLACK, [100, 190], [x, 220], 1)
	x += 55 / 3
#boat
rect(screen, BROWN, (280, 180, 120, 30))
polygon(screen, BROWN, ((400, 180), (460, 180), (400, 210)))
circle(screen, BROWN, (280, 180), 30)
rect(screen, SEA_BLUE, (250, 150, 100, 30))
rect(screen, BLACK, (330, 100, 5, 80))
polygon(screen, BEIGE, ((335, 100), (385, 140), (345,140)))
polygon(screen, BLACK, ((335, 100), (385, 140), (345,140)), 1)
polygon(screen, BEIGE, ((335, 180), (385, 140), (345,140)))
polygon(screen, BLACK, ((335, 180), (385, 140), (345,140)), 1)
circle(screen, WHITE, (412, 192), 10)
circle(screen, BLACK, (412, 192), 10, 3)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()