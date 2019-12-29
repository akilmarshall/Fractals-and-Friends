'''
This file contains functions that create and concern polygons
Polygons are defined as a list of vertices
'''

from math import pi, cos, sin
from random import choice
import pygame


class Polygon():

    """Polygon implementaion"""

    def __init__(self, h, k, r, n):
        """TODO: to be defined.

        :h: x-coord of the polygon's center
        :k: y-coord of the polygon's center
        :r: internal radius of the polygon
        :n: number of vertices
        :phi: rotational offset from the positive x-axis

        """

        self.h = h
        self.k = k
        self.r = r
        self.n = n
        self.vertices = list()

        for i in range(self.n):
            theta = (((2 * pi) / self.n) * i) - pi/2
            x = h + (self.r * cos(theta))
            y = k + (self.r * sin(theta))
            self.vertices.append((int(x), int(y)))

    def __repr__(self):
        return f'Polygon({self.h}, {self.k}, {self.r}, {self.n})'

    def __len__(self):
        return self.n

    def __contains__(self, item):
        x, y = item
        j = self.n - 1
        c = False
        for i in range(self.n):
            if ((self.vertices[i][1] > y) != (self.vertices[j][1] > y)) and (x < self.vertices[i][0] + (self.vertices[j][0] - self.vertices[i][0]) * (y - self.vertices[i][1]) / (self.vertices[j][1] - self.vertices[i][1])):
                c = not c
            j = i
        return c

    def random_point(self):
        '''
        returns a random point interior to the polygon
        '''
        def random_point_near_polygon(p: Polygon):
            max_x = max([x for (x, y) in p.vertices])
            max_y = max([y for (x, y) in p.vertices])
            min_x = min([x for (x, y) in p.vertices])
            min_y = min([y for (x, y) in p.vertices])
            x = choice(range(min_x, max_x + 1))
            y = choice(range(min_y, max_y + 1))
            return (x, y)

        while True:
            a = random_point_near_polygon(self)
            if a in self:
                return a


# def translate(V: list, p) -> list:
def translate(p, t) -> Polygon:
    '''
    t is a point in R^2
    p is a Polygon
    t is a description of the translation
    '''
    o = Polygon(p.h, p.k, p.r, p.n)  # ghetto deep copy
    tx, ty = t
    tx = int(tx)
    ty = int(ty)
    o.vertices = [(x + tx, y + ty) for x, y in p.vertices]
    return o


def scale(p: Polygon, s: float) -> Polygon:
    '''
    Each point in p will be scaled by s
    '''
    o = Polygon(p.h, p.k, s * p.r, p.n)
    return o

def rotate(p: Polygon, phi: float) -> Polygon:
    '''
    Rotate the polgon p by phi radians
    '''
    o = Polygon(p.h, p.k, p.r, p.n)

    for i in range(p.n):
        theta = (((2 * pi) / p.n) * i) - pi/2
        x = p.h + (p.r * cos(theta + phi))
        y = p.k + (p.r * sin(theta + phi))
        o.vertices[i] = (int(x), int(y))

    o.vertices = [(int(x), int(y)) for x, y in o.vertices]

    return o

def shear(p: Polygon, m: float) -> Polygon:
    '''
    Shear the polygon p with shear factor m
    '''
    o = Polygon(p.h, p.k, p.r, p.n)
    o.vertices = [(x + (m * y), y) for x, y in p.vertices]
    o.vertices = [(int(x), int(y)) for x, y in o.vertices]
    return o

def reflect(p: Polygon, m: float, b: float) -> Polygon:
    '''
    reflect polygon p across the line y = mx + b
    '''
    def reflect_x(x, y):
        return (((1 - m**2) * x) + (2 * m * y) - (2 * m * b)) / (m**2 + 1)

    def reflect_y(x, y):
        return (((m**2 - 1) * y) + (2 * m * x) - (2 * b)) / (m**2 + 1)
        
    o = Polygon(p.h, p.k, p.r, p.n)
    o.vertices = [(reflect_x(x, y), reflect_y(x, y)) for x, y in p.vertices]
    o.vertices = [(int(x), int(y)) for x, y in o.vertices]
    return o


if __name__ == "__main__":
    pygame.init()

    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)

    canvas_width = 500
    canvas_height = 500
    canvas = pygame.display.set_mode((canvas_width, canvas_height))
    canvas.fill(black)
    
    pixels = pygame.PixelArray(canvas)

    # code here

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
