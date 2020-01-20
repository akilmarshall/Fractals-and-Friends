import math
import pygame
import chaos_game
import polygons
import draw

pygame.init()

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
canvas.fill(draw.BASE03)

'''
# flip a triangle by pi and move it such that it tiles the sub triangles
rows = 2
cols = 4
# info = draw.grid_info(CANVAS_WIDTH, CANVAS_HEIGHT, cols, rows)
h, k = CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2
r = 400
poly = polygons.Polygon(h, k, r, 3)
l = r
poly2 = polygons.rotate(polygons.Polygon(h , k+ (r / 4), 400, 3), math.pi)
triangle1 = chaos_game.chaos_game(poly, 1/2, 100000)
triangle2 = chaos_game.chaos_game(poly2, 1/2, 100000)
# draw.draw_list(triangle, canvas, color=draw.CYAN)
draw.draw_lists([triangle1, triangle2], canvas, [draw.CYAN, draw.GREEN])
'''
def tessellate_triangle_line(h, k, R, n, step=1/2, points=100000):
    r = R / 2
    a = math.sqrt(3) * R
    poly = polygons.Polygon(h, k, R, 3)
    line = list()
    for i in range(n):
        poly = polygons.rotate(poly, i * math.pi)
        poly = polygons.translate(poly, (i * (a / 2), 0))
        if i % 2:
            poly = polygons.translate(poly, (0, -r))
        triangle = chaos_game.chaos_game(poly, step, points, cast=True)
        line.append(triangle)

    return line


def tessellate_triangle_grid(row, col, colors, h, k, R, step=1/2, points=100000):
    for r in range(row):
        draw.draw_lists(tessellate_triangle_line(h, k + (r * (1.5 * R)), R, col, points=points), canvas, colors)
        colors = [colors[-1]] + colors[:-1]


def tessellate_hexagon_line(h, k, R, n, step=2/3, points=100000):
    # r = R / 2
    # a = math.sqrt(3) * R
    poly = polygons.Polygon(h, k, R, 6)
    line = list()
    for i in range(n):
        hexagon = chaos_game.chaos_game_2(poly, step, points)
        poly = polygons.translate(poly, (R * math.sqrt(3), 0))
        line.append(hexagon)

    return line

def tessellate_hexagon_grid(row, col, colors, h, k, R, step=2/3, points=100000):
    for r in range(row):
        draw.draw_lists(tessellate_hexagon_line(h, k, R, col, step=step, points=points), canvas, colors)
        if r % 2:
            h += R * math.sqrt(3) * math.sin(math.pi / 6)
        else:
            h -= R * math.sqrt(3) * math.sin(math.pi / 6)
        k += R * math.sqrt(3) * math.cos(math.pi / 6)
        colors = [colors[-1]] + colors[:-1]


h, k = (0, 0)
r = 50
# colors = draw.COLORS
# colors = [draw.RED, draw.YELLOW, draw.BLUE]
# colors = [draw.MAGENTA, draw.CYAN]
colors = [draw.CYAN, draw.BLUE]
row = 12
col = 11
tessellate_hexagon_grid(row, col, colors, h, k, r, points=10000)
# tessellate_triangle_grid(row, col, colors, h, k, r, points=10000)

pygame.image.save(canvas, 'out.png')  # saves a picture

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
