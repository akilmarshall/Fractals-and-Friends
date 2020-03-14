import math
import pygame
import chaos_game
import polygons
import draw

pygame.init()

def tessellate_triangle_line(h, k, R, n, step=1/2, points=100000, game=chaos_game.chaos_game):
    r = R / 2
    a = math.sqrt(3) * R
    poly = polygons.Polygon(h, k, R, 3)
    line = list()
    for i in range(n):
        poly = polygons.rotate(poly, i * math.pi)
        poly = polygons.translate(poly, (i * (a / 2), 0))
        if i % 2:
            poly = polygons.translate(poly, (0, -r))
        triangle = game(poly, step, points, cast=True)
        line.append(triangle)

    return line


def tessellate_triangle_grid(row, col, colors, h, k, R, step=1/2, points=100000, game=chaos_game.chaos_game):
    for r in range(row):
        draw.draw_lists(tessellate_triangle_line(h, k + (r * (1.5 * R)), R, col, points=points, game=game), canvas, colors)
        colors = [colors[-1]] + colors[:-1]


def tessellate_hexagon_line(h, k, R, n, step=2/3, points=100000, game=chaos_game.chaos_game):
    poly = polygons.Polygon(h, k, R, 6)
    poly = polygons.rotate(poly, math.pi / 3)
    line = list()
    for i in range(n):
        hexagon = game(poly, step, points)
        poly = polygons.translate(poly, (R * math.sqrt(3), 0))
        line.append(hexagon)

    return line

def tessellate_hexagon_grid(row, col, colors, h, k, R, step=2/3, points=100000, game=chaos_game.chaos_game):
    for r in range(row):
        draw.draw_lists(tessellate_hexagon_line(h, k, R, col, step=step, points=points, game=game), canvas, colors)
        if r % 2:
            h += R * math.sqrt(3) * math.sin(math.pi / 6)
        else:
            h -= R * math.sqrt(3) * math.sin(math.pi / 6)
        k += R * math.sqrt(3) * math.cos(math.pi / 6)
        colors = [colors[-1]] + colors[:-1]


def tessellate_cube_line(h, k, R, n, step=1/2, points=100000, game=chaos_game.chaos_game_2):
    poly = polygons.Polygon(h, k, R, 4)
    poly = polygons.rotate(poly, math.pi / 3)
    line = list()
    for i in range(n):
        cube = game(poly, step, points)
        poly = polygons.translate(poly, (R * math.sqrt(2), 0))
        line.append(cube)
    return line


def tessellate_cube_grid(row, col, colors, h, k, R, step=1/2, points=100000, game=chaos_game.chaos_game_2):
    for r in range(row):
        draw.draw_lists(tessellate_cube_line(h, k, R, col, step=step, points=points, game=game), canvas, colors)
        k += R * math.sqrt(2)
        colors = [colors[-1]] + colors[:-1]

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
canvas.fill(draw.BLACK)

h, k = (0, 0)
r = 250
colors = [draw.RED]
colors = [draw.RED, draw.YELLOW, draw.BLUE]
colors = [draw.YELLOW, draw.ORANGE, draw.RED]
colors = draw.COLORS
colors = [draw.MAGENTA, draw.BLUE, draw.RED]
colors = [draw.MAGENTA, draw.CYAN]
colors = [draw.CYAN, draw.GREEN, draw.BLUE]
row = 12
col = 12
tessellate_cube_grid(row, col, [draw.WHITE], h, k, r, step=1/2, points=100000, game=chaos_game.chaos_game)
# tessellate_hexagon_grid(row, col, colors, h, k, r, points=10000, game=chaos_game.chaos_game)
tessellate_triangle_grid(row, col, [draw.CYAN], h, k, r, points=100000, game=chaos_game.chaos_game)
# tessellate_cube_grid(row, col, [draw.BLACK], h, k, r, step=1/2, points=100000, game=chaos_game.chaos_game_2)

pygame.image.save(canvas, 'out.png')  # saves a picture

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
