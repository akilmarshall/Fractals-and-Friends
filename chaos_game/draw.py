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

BASE03 = (0, 43, 54)
BASE02 = (7, 54, 66)
BASE01 = (88, 110, 117)
BASE00 = (101, 123, 131)
BASE0 = (131, 148, 150)
BASE1 = (147, 161, 161)
BASE2 = (238, 232, 213)
BASE3 = (253, 246, 227)


COLORS = [YELLOW, ORANGE, RED, MAGENTA, VIOLET, BLUE, CYAN, GREEN]


def draw_list(points: list, canvas: pygame.display, color=MAGENTA):
    '''
    given a list of 2D points and pygame.PixelArray
    this function will set the color of those points in the array
    '''
    pixels = pygame.PixelArray(canvas)
    limit_x = len(pixels)
    limit_y = len(pixels[0])
    for x, y in points:
        # bounds checking
        if (x < 0) or (x >= limit_x) or (y < 0) or (y >= limit_y):
            continue
        pixels[x][y] = color
    pixels.close()

def draw_lists(point_list: list, canvas: pygame.display, color=MAGENTA):
    for l in point_list:
        draw_list(l, canvas, color=color)

def grid_info(canvas_width: int, canvas_height: int, cols: int, rows: int) -> dict:
    pad = 5
    info = dict()

    x = canvas_width / (2 * cols)
    y = canvas_height / (2 * rows)
    info['radius'] = int(min(x, y)) - pad

    delta_x = canvas_width / cols
    delta_y = canvas_height / rows
    centers = list()
    for j in range(rows):
        for i in range(cols):
            h = int(x + (i * delta_x))
            k = int(y + (j * delta_y))
            centers.append((h, k))

    info['centers'] = centers
    return info


if __name__ == "__main__":
    pygame.init()

    CANVAS_WIDTH = 1800
    CANVAS_HEIGHT = 1000
    canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    canvas.fill(BASE03)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
