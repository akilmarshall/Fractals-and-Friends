'''
This file contains functions that create and concern polygons
Polygons are defined as a list of vertices
'''
import pygame
from math import pi, cos, sin
from random import choice


def equilateral_triangle(a, x):
    ax, ay = a
    return [(ax, ay), (ax, ay + x), (ax + x, ay + x)]


def regular_polygon(A, n, l, phi=pi/2):
    '''
    returns a list of vertices describing a regular polygon about A with n vertices and internal radius of l
    phi is the offset from the positive x-axis
    '''
    vertices = list()
    x, y = A
    for i in range(n):
        theta = (((2 * pi) / n) * i) - phi
        h = x + (l * cos(theta))
        k = y + (l * sin(theta))
        vertices.append((int(h), int(k)))
    return vertices


def point_in_polygon(a, P):
    x, y = a
    num = len(P)
    j = num - 1
    c = False
    for i in range(num):
        if ((P[i][1] > y) != (P[j][1] > y)) and (x < P[i][0] + (P[j][0] - P[i][0]) * (y - P[i][1]) / (P[j][1] - P[i][1])):
            c = not c
        j = i
    return c


def random_point_in_polygon(P):

    def random_point_near_polygon(P):
        max_x = max([x for (x, y) in P])
        max_y = max([x for (x, y) in P])
        min_x = min([x for (x, y) in P])
        min_y = min([x for (x, y) in P])
        x = choice(range(min_x, max_x))
        y = choice(range(min_y, max_y))
        return (x, y)

    while True:
        a = random_point_near_polygon(P)
        if point_in_polygon(a, P):
            return a


if __name__ == "__main__":
    pygame.init()

    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 255)

    canvas_width = 500
    canvas_height = 500
    canvas = pygame.display.set_mode((canvas_width, canvas_height))
    canvas.fill(black)

    pixels = pygame.PixelArray(canvas)

    a = random_point_in_polygon(regular_polygon((250, 250), 3, 100))
    P = regular_polygon((250, 250), 3, 100)
    pygame.draw.polygon(canvas, white, P)
    x, y = a
    pixels[x][y] = blue

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
