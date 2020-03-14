import itertools
import math
import pygame
import chaos_game
import polygons
import draw

pygame.init()

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
canvas.fill(draw.WHITE)

# font = pygame.font.Font(pygame.font.get_default_font(), 20)

h,k = (CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
poly = polygons.rotate(polygons.Polygon(h, k, 300, 4), math.pi / 4)
D4 = chaos_game.chaos_game_3(poly, 1/2, 100000, cast=True)
poly_ = polygons.scale(poly, 1 + 10**-2)
poly_ = polygons.rotate(poly_, math.pi / 4)
pygame.draw.polygon(canvas, draw.BLACK, poly_.vertices)
pygame.draw.polygon(canvas, draw.WHITE, poly.vertices)
draw.draw_list(D4, canvas, color=draw.BLACK)

# one = font.render('1', True, draw.BLACK)
# two = font.render('2', True, draw.BLACK)
# three = font.render('3', True, draw.BLACK)
# four = font.render('4', True, draw.BLACK)
# canvas.blit(one, (h - 165, k - 210))
# canvas.blit(two, (h + 200, k - 180))
# canvas.blit(three, (h + 165, k + 195))
# canvas.blit(four, (h - 210, k + 165))

# pygame.image.save(canvas, 'out.png')  # saves a picture

sin = list()
x = 0
while True:
    a, b = (200*math.cos(x), 200*math.sin(x))
    sin.append((a, b))
    draw.draw_list(sin, canvas, color=draw.BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
    x += 1
