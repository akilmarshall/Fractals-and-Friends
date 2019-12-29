
from random import choice
from math import pi, sin
import pygame
from Polygons import Polygon


def chaos_game(P, d, n):
    a = random_point_in_polygon(P)
    for _ in range(n):
        x0, y0 = a
        x1, y1 = choice(P)
        delta_x = int((x1 - x0) * d)
        delta_y = int((y1 - y0) * d)
        h = delta_x + x0
        k = delta_y + y0
        a = (h, k)
        yield a


def draw_chaos_game(points, pixels, color=(211, 54, 130)):
    for x, y in points:
        pixels[x][y] = color


def restricted_chaos_game(P, d, n):
    a = random_point_in_polygon(P)
    v = choice(P)
    for _ in range(n):
        x0, y0 = a
        v = choice(list(filter(lambda x: x != v, P)))
        x1, y1 = v
        delta_x = int((x1 - x0) * d)
        delta_y = int((y1 - y0) * d)
        h = delta_x + x0
        k = delta_y + y0
        a = (h, k)
        yield a


def restricted_chaos_game_2(P, d, n):
    a = random_point_in_polygon(P)
    v = choice(P)
    for _ in range(n):
        x0, y0 = a
        index = (P.index(v) - 1) % len(P)
        v = choice(P[0:index] + P[index + 1:])
        x1, y1 = v
        delta_x = int((x1 - x0) * d)
        delta_y = int((y1 - y0) * d)
        h = delta_x + x0
        k = delta_y + y0
        a = (h, k)
        yield a


def chaos_game_over_polygons(P, d, n, epsilon=1000):
    p = choice(P)
    a = random_point_in_polygon(p)
    for _ in range(n):
        if choice(range(epsilon)):
            p = choice(P)
        x0, y0 = a
        x1, y1 = choice(p)
        delta_x = int((x1 - x0) * d)
        delta_y = int((y1 - y0) * d)
        h = delta_x + x0
        k = delta_y + y0
        a = (h, k)
        yield a


def barnsley_fern(n, scale=-30, x_off=250, y_off=400):
    sequence = [(0, 0)]

    def f1(x, y, a=0, b=0, c=0, d=0.16, e=0, f=0):
        x = (a * x) + (b * y)
        y = (c * x) + (d * y)
        return (x, y)

    def f2(x, y, a=0.85, b=0.04, c=-0.04, d=0.85, e=0, f=1.6):
        x = (x * d) + (b * y)
        y = (x * c) + (d * y) + f
        return (x, y)

    def f3(x, y, a=0.2, b=-0.26, c=0.23, d=0.22, e=0, f=1.6):
        x = (x * d) + (b * y)
        y = (x * c) + (d * y) + f
        return (x, y)

    def f4(x, y, a=-0.15, b=0.28, c=0.26, d=0.24, e=0, f=0.44):
        x = (x * d) + (b * y)
        y = (x * c) + (d * y) + f
        return (x, y)

    for _ in range(n):
        roll = choice(range(100))
        if roll == 0:
            # do f1
            x, y = sequence[-1]
            sequence.append(f1(x, y))
        elif 1 <= roll <= 85:
            # do f2
            x, y = sequence[-1]
            sequence.append(f2(x, y))
        elif 86 <= roll <= 93:
            # do f3
            x, y = sequence[-1]
            sequence.append(f3(x, y))
        elif 93 <= roll <= 99:
            # do f4
            x, y = sequence[-1]
            sequence.append(f4(x, y))

    B = [(round(x * scale) + x_off, round(y * scale) + y_off) for x, y in sequence]
    return B


if __name__ == "__main__":
    pygame.init()

    white = (255, 255, 255)
    black = (0, 0, 0)

    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    magenta = (211, 54, 130)

    canvas_width = 500
    canvas_height = 500
    canvas = pygame.display.set_mode((canvas_width, canvas_height))
    canvas.fill(black)

    pixels = pygame.PixelArray(canvas)

    '''
    center = (canvas_width / 2, canvas_height / 2)  # center of the chaos game
    n = 4  # number of vertices
    l = 200  # distance from vertices to center
    P = regular_polygon(center, n, l, phi=pi/4)  # polygon to house the chaos game
    x, y = center
    delta = int(200*sin(pi/4))
    P = P + [(x, y + delta), (x, y - delta), (x + delta, y), (x - delta, y)]
    step = 2/3
    '''
    B = barnsley_fern(100000)
    draw_chaos_game(B, pixels, color=(133, 153, 0))

    # drawing the points in the sequence
    # draw_chaos_game(chaos_game(P, step, 100000), pixels)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
