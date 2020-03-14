import pygame
import chaos_game
import polygons
import draw

pygame.init()

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
canvas.fill(draw.BASE03)

# code here

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
