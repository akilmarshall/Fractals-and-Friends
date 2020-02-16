from math import pi
from random import choice
import pygame
from . import polygons
from . import draw

def chaos_game(p: polygons.Polygon, step: float, n: int, cast=False):
    '''
    :p:     polygon parameter of the chaos game
    :step:  step size parameter of the chaos game
    :n:     the number of iterations to run the chaos game
    :cast: boolean flag to either round or cast coordinates to int
    description
    1. Pick a random point within the polygon
    2. Pick a random vertex
    3. Step a predetermined fraction of the distance towards the vertex
    4. Store the spatial position
    5. Go to 2
    '''
    cur = p.random_point()  # the current step in the sequence, initialized to a random point

    for _ in range(n):
        a, b = cur
        c, d = choice(p.vertices)
        delta_x = (c - a) * step
        delta_y = (d - b) * step
        if cast:
            delta_x = int(delta_x)
            delta_y = int(delta_y)
        else:
            delta_x = round(delta_x)
            delta_y = round(delta_y)
        cur = (delta_x + a, delta_y + b)
        yield cur


def chaos_game_2(p: polygons.Polygon, step: float, n: int, cast=False):
    '''
    :p:     polygon parameter of the chaos game
    :step:  step size parameter of the chaos game
    :n:     the number of iterations to run the chaos game
    description
    1. Pick a random point within the polygon
    2. Pick a random vertex excluding the previously selected vertex
    3. Step a predetermined fraction of the distance towards the vertex
    4. Store the spatial position
    5. Go to 2
    '''
    cur = p.random_point()
    v = choice(p.vertices)
    for _ in range(n):
        a, b = cur
        v = choice(list(filter(lambda x: x != v, p.vertices)))  # filter the previous vertex
        c, d = v
        delta_x = (c - a) * step
        delta_y = (d - b) * step
        if cast:
            delta_x = int(delta_x)
            delta_y = int(delta_y)
        else:
            delta_x = round(delta_x)
            delta_y = round(delta_y)
        cur = (delta_x + a, delta_y + b)
        yield cur


def chaos_game_3(p: polygons.Polygon, step: float, n: int, cast=False):
    '''
    :p:     polygon parameter of the chaos game
    :step:  step size parameter of the chaos game
    :n:     the number of iterations to run the chaos game
    description
    1. Pick a random point within the polygon
    2. Pick a random vertex with rotational position that is anti-clockwise of the previous vertex
    3. Step a predetermined fraction of the distance towards the vertex
    4. Store the spatial position
    5. Go to 2
    '''
    cur = p.random_point()
    v = choice(p.vertices)
    for _ in range(n):
        a, b = cur
        index = (p.vertices.index(v) - 1) % len(p.vertices)
        v = choice(p.vertices[0:index] + p.vertices[index + 1:])
        c, d = v
        delta_x = (c - a) * step
        delta_y = (d - b) * step
        if cast:
            delta_x = int(delta_x)
            delta_y = int(delta_y)
        else:
            delta_x = round(delta_x)
            delta_y = round(delta_y)
        cur = (delta_x + a, delta_y + b)
        yield cur



def sierpinski_carpet(p: polygons.Polygon, step: float, n: int, cast=False):
    '''
    :p:     polygon parameter of the chaos game
    :step:  step size parameter of the chaos game
    :n:     the number of iterations to run the chaos game
    description
    1. Pick a random point within the polygon
    2. Pick a random vertex, mid points between neigboring vertices included
    3. Step a predetermined fraction of the distance towards the vertex
    4. Store the spatial position
    5. Go to 2
    '''
    def mid_points(l: list) -> list:
        lprime = l[1:] + [l[0]]
        return [((a + c) / 2, (d + b) / 2) for (a, b), (c, d) in zip(l, lprime)]

    cur = p.random_point()  # the current step in the sequence, initialized to a random point

    for _ in range(n):
        a, b = cur
        c, d = choice(p.vertices + mid_points(p.vertices))
        delta_x = (c - a) * step
        delta_y = (d - b) * step
        if cast:
            delta_x = int(delta_x)
            delta_y = int(delta_y)
        else:
            delta_x = round(delta_x)
            delta_y = round(delta_y)
        cur = (delta_x + a, delta_y + b)
        yield cur


def vicsek_fractal(p: polygons.Polygon, step: float, n: int, cast=False):
    '''
    :p:     polygon parameter of the chaos game
    :step:  step size parameter of the chaos game
    :n:     the number of iterations to run the chaos game
    description
    1. Pick a random point within the polygon
    2. Pick a random vertex
    3. Step a predetermined fraction of the distance towards the vertex
    4. Store the spatial position
    5. Go to 2
    '''
    cur = p.random_point()  # the current step in the sequence, initialized to a random point

    for _ in range(n):
        a, b = cur
        c, d = choice(p.vertices + [(p.h, p.k)])
        delta_x = (c - a) * step
        delta_y = (d - b) * step
        if cast:
            delta_x = int(delta_x)
            delta_y = int(delta_y)
        else:
            delta_x = round(delta_x)
            delta_y = round(delta_y)
        cur = (delta_x + a, delta_y + b)
        yield cur

def barnsley_fern(n, scale=-30, x_off=250, y_off=400, cast=False):
    '''
    TODO
    '''
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
        if roll == 0:  # 1% chance
            # do f1
            x, y = sequence[-1]
            sequence.append(f1(x, y))
        elif 1 <= roll <= 85:  # 85% chance
            # do f2
            x, y = sequence[-1]
            sequence.append(f2(x, y))
        elif 86 <= roll <= 93:  # 7% chance
            # do f3
            x, y = sequence[-1]
            sequence.append(f3(x, y))
        elif 93 <= roll <= 99:  # 7% chance
            # do f4
            x, y = sequence[-1]
            sequence.append(f4(x, y))

    # adjust points to integers
    fern = [(x * scale + x_off, y * scale + y_off) for x, y in sequence]
    if cast:
        fern = ((int(x), int(y)) for x, y in fern)
    else:
        fern = ((round(x), round(y)) for x, y in fern)
    return fern


if __name__ == "__main__":
    pygame.init()


    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 400
    canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    canvas.fill(draw.BLACK)

    h = CANVAS_WIDTH / 2
    k = CANVAS_HEIGHT / 2
    P = polygons.Polygon(h, k, 200, 3)
    C = chaos_game(P, 1/2, 10000)
    draw.draw_list(C, canvas, color=draw.BLUE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
