from math import pi
import pygame
from chaos_game import polygons, chaos_game, draw

pygame.init()

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
canvas.fill(draw.BASE03)

# draw text

color = (170, 170, 170)
# color = draw.BASE03
def word_stripe(word: str, pos: tuple, step: tuple, n: int):
    h, k = pos
    delta_x, delta_y = step
    h, k = h - (n * delta_x), k - (n * delta_y)
    points = [(h + (i * delta_x), k + (i * delta_y)) for i in range((2 * n) - 1)]
    font = pygame.font.Font(pygame.font.get_default_font(), 40)
    text = font.render(word, True, color)
    for x, y in points:
        canvas.blit(text, (x, y))

h = (CANVAS_WIDTH / 2) - 300
k = (CANVAS_HEIGHT / 2) - 50

font = pygame.font.Font(pygame.font.get_default_font(), 40)
text = font.render('If loving you is', True, color)

# word_stripe('wrong', (h + 290, k), (10, 25), 5)
# canvas.blit(text, (h, k))
# h += 230
# k += 130
# text = font.render('am I wrong to', True, color)
# word_stripe('fall?', (h + 270, k), (-10, 30), 5)
# canvas.blit(text, (h, k))

# draw background

tile_size = 80

# draw an nxn grid
origin_x, origin_y = (0, 0)
n = 26
tiles = list()
for x in [tile_size * i for i in range(n)]:
    for y in [tile_size * i for i in range(n)]:
        P = polygons.Polygon(x, y, tile_size, 4)
        # P = polygons.rotate(P, pi/6)
        C = chaos_game.chaos_game_3(P, 1/2, 1000)
        tiles.append(C)
draw.draw_lists(tiles, canvas, [draw.YELLOW])

pygame.image.save(canvas, 'default.png')  # saves a picture

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
