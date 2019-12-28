import pygame
import chaos_game

pygame.init()

black = (0, 0, 0)
blue = (38, 139, 210)
yellow = (181, 137, 0)
red = (220, 50, 47)
green = (153, 0, 68)
violet = (108, 113, 196)
magenta = (211, 54, 130)

canvas_width = 500
canvas_height = 500
canvas = pygame.display.set_mode((canvas_width, canvas_height))
canvas.fill(black)

# code here

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()

