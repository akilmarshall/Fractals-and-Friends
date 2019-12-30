'''
draw.py
contains functions that draw to the screen
'''
import itertools
import pygame
import chaos_game
import polygons

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

YELLOW = (181, 137, 0)
ORANGE = (203, 75, 22)
RED = (220, 50, 47)
MAGENTA = (211, 54, 130)
VIOLET = (108, 113, 196)
BLUE = (38, 139, 210)
CYAN = (42, 161, 152)
GREEN = (133, 153, 0)

COLORS = [YELLOW, ORANGE, RED, MAGENTA, VIOLET, BLUE, CYAN, GREEN]


def draw_list(points: list, pixels: pygame.PixelArray, color=MAGENTA):
    '''
    given a list of 2D points and pygame.PixelArray
    this function will set the color of those points in the array
    '''
    for x, y in points:
        pixels[x][y] = color

def draw_lists(point_list: list, pixels, color=MAGENTA):
    for l in point_list:
        draw_list(l, pixels, color=color)

def grid_info(canvas_width: int, canvas_height: int, cols: int, rows: int, frame=100, pad=50) -> dict:
    canvas_width = canvas_width - (2 * frame)
    canvas_height = canvas_height - (2 * frame)
    info = dict()

    x = canvas_width / (2 * cols)
    y = canvas_height / (2 * rows)
    info['radius'] = min(x, y) - pad

    delta_x = canvas_width / cols
    delta_y = canvas_height / rows
    centers = list()
    for j in range(cols):
        k = y + (j * delta_y)
        for i in range(rows):
            h = x + (i * delta_x)
            centers.append((h, k))

    info['centers'] = centers
    return info


if __name__ == "__main__":
    pygame.init()

    CANVAS_WIDTH = 1800
    CANVAS_HEIGHT = 1000
    canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    canvas.fill(BLACK)
    pixels = pygame.PixelArray(canvas)

    info = grid_info(CANVAS_WIDTH, CANVAS_HEIGHT, 2, 2)
    polys = [polygons.Polygon(h, k, info['radius'], 3) for h, k in info['centers']]
    # draw_lists([p.vertices for p in polys], pixels)
    for p in polys:
        pygame.draw.polygon(canvas, CYAN, p.vertices)
    centers = [(int(p.h), int(p.k)) for p in polys]
    print(centers)
    draw_list(centers, pixels, color=BLACK)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
