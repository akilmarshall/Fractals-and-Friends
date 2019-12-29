from math import pi
from random import choice
import pygame
import Polygons


black = (0, 0, 0)
blue = (38, 139, 210)
yellow = (181, 137, 0)
red = (220, 50, 47)
green = (153, 0, 68)
violet = (108, 113, 196)
magenta = (211, 54, 130)


class ChaosGame():

    """Base class for chaos games"""

    def __init__(self, p: Polygons.Polygon, step: float, n: int, color=blue):
        """ Intialize the parameters for the chaos game

        :P: P is an iterable of 2D points describing the vertices of a polygon
        :step: A real number in (-1, 1) describing the step size per iteration
        :n: The number of iterations to take in the chaos game
        :color: Color to use when drawing the game
        """
        self.polygon = p
        self.step = step
        self.n = n
        self.color = color
        self.sequence = list()  # stores the last played chaos game

        # generate the sequence
        self.game()

    def __repr__(self):
        return f'ChaosGame({self.polygon}, {self.step}, {self.n}, color={self.color})'

    def game(self):
        a = self.polygon.random_point()
        for _ in range(self.n):
            x0, y0 = a
            x1, y1 = choice(self.polygon.vertices)
            delta_x = int((x1 - x0) * self.step)
            delta_y = int((y1 - y0) * self.step)
            h = delta_x + x0
            k = delta_y + y0
            a = (h, k)
            self.sequence.append(a)

    # def sequence(self):
    #     '''Yield each step of the sequence'''
    #     if len(self.sequence) != 0:
    #         for p in self.sequence:
    #             yield p

    def draw(self, pixels):
        '''
        :pixels: is a pygame.PixelArray
        '''
        for x, y in self.sequence:
            pixels[x][y] = self.color

    def translate(self, t: tuple):
        '''
        translate self.polygon by t. Where t is a description of the translation
        '''
        x, y = t
        self.polygon = Polygons.translate(self.polygon, (x, y))
        self.game()

    def scale(self, s: float):
        '''
        scale self.polygon by the parameter s
        '''
        self.polygon = Polygons.scale(self.polygon, s)
        self.game()

    def rotate(self, phi: float):
        self.polygon = Polygons.rotate(self.polygon, phi)
        self.game()

    def shear(self, m: float):
        old = self.polygon
        p = Polygons.Polygon(old.h, old.k, old.r, old.n)
        p = Polygons.shear(p, m)
        self.polygon = p
        self.game()
        # self.polygon = Polygons.shear(self.polygon, m)
        # self.game()

    def reflect(self, m: float, b: float):
        self.polygon = Polygons.reflect(self.polygon, m, b)
        self.game()

def chaos_game(P, d, n):
    a = P.random_point()
    for _ in range(n):
        x0, y0 = a
        x1, y1 = choice(P)
        delta_x = int((x1 - x0) * d)
        delta_y = int((y1 - y0) * d)
        h = delta_x + x0
        k = delta_y + y0
        a = (h, k)
        yield a

def ChaosGame(p: Polygons.Polygon, step: float, n: int):
    '''
    :p: polygon parameter of the chaos game
    :step: step size parameter of the chaos game
    :n: the number of iterations to run the chaos game
    '''
    cur = p.random_point()  # the current step in the sequence, intialized to a random point

    for _ in range(n):
        a, b = cur
        c, d = choice(p.vertices)
        delta_x = int((c - a) * step)
        delta_y = int((d - b) * step)
        cur = (delta_x + a, delta_y + b)
        yield cur


'''
def draw_chaos_game(points, pixels, color=(211, 54, 130)):
    for x, y in points:
        pixels[x][y] = color
'''

def DrawList(points: list, pixels: pygame.PixelArray, color=(211, 54, 130)):
    for x, y in points:
        pixels[x][y] = color
'''

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
'''

def ChaosGame2(p: Polygons.Polygon, step: float, n: int):
    cur = p.random_point()
    v = choice(p.vertices)
    for _ in range(n):
        a, b = cur
        v = choice(list(filter(lambda x: x != v, p.vertices)))  # filter the previous vertice
        c, d = v
        delta_x = int((c - a) * step)
        delta_y = int((d - b) * step)
        cur = (delta_x + a, delta_y + b)
        yield cur

'''
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
'''
def ChaosGame3(p: Polygons.Polygon, step: float, n: int):
    cur = p.random_point()
    v = choice(p.vertices)
    for _ in range(n):
        a, b = cur
        index = (p.vertices.index(v) - 1) % len(p.vertices)
        v = choice(p.vertices[0:index] + p.vertices[index + 1:])
        c, d = v
        delta_x = int((c - a) * step)
        delta_y = int((d - b) * step)
        cur = (delta_x + a, delta_y + b)
        yield cur
'''

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

'''
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

    B = [(int(x * scale) + x_off, int(y * scale) + y_off) for x, y in sequence]
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

    P = Polygons.Polygon(250, 250, 250, 4)
    # points = chaos_game(P, 1/2, 1000)
    # p1 = ChaosGame3(Polygons.translate(Polygons.shear(P, 0.7), (-200, 0)), 1/2, 100000)

    # DrawList(p1, pixels)
    fern = barnsley_fern(10000)
    DrawList(fern, pixels)
    
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
