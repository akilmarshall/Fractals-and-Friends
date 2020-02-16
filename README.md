# Fractals and Friends
 A framework for my exploration and research of fractals and kindred self similar processes/structures. Written in python with heavy usage of [pygame](https://www.pygame.org/wiki/about)

## Todo
- [ ] <s>Convert api to object oriented</s>
- [x] Implement geometric transformations ([info](https://www.cs.brandeis.edu/~cs155/Lecture_06.pdf))
    - [x] [Rigid](https://en.wikipedia.org/wiki/Rigid\_transformation)
    - [x] [Similarity](https://en.wikipedia.org/wiki/Similarity_geometry)
    - [x] [Affine](https://en.wikipedia.org/wiki/Affine_transformation)
- [x] implement bulk visualizations
    - [ ] cell labeling api
        - [ ] caption
        - [ ] title
- [ ] use chaos games as textures
    - [ ] implement 3D polygons
    - [ ] use the geometry to run chaos games on the surfaces
    - [ ] render the polygons
- [ ] describe the draw.grid_info function and the methodology for grid visualizations in the Grid Visualizations section

## Boilerplate
```python
import pygame
from chaos_game import polygons, chaos_game, draw

pygame.init()

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
canvas.fill(draw.BASE03)

# code here

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
```

## Chaos game
[source](https://en.wikipedia.org/wiki/Chaos_game) and [source](https://youtu.be/kbKtFN71Lfs)

To match the Wikipedia pictures of regular polygons where n = 4, set phi = pi/4 

### Sierpinski Triangle
Let n = 3 and step = 1/2.

```python
h = CANVAS_WIDTH / 2
k = CANVAS_HEIGHT / 2
P = polygons.Polygon(h, k, 200, 3)
C = chaos_game.chaos_game(P, 1/2, 100000)
draw.draw_list(C, canvas, color=draw.BLUE)
```
![Sierpinski triangle](https://i.imgur.com/Dwwa4rT.png)

----

Let n = 6 and step = 2/3.

```python
h = CANVAS_WIDTH / 2
k = CANVAS_HEIGHT / 2
P = polygons.Polygon(h, k, 200, 6)
C = chaos_game.chaos_game(P, 2/3, 100000)
draw.draw_list(C, canvas, color=draw.YELLOW)
```
![Chaos game](https://i.imgur.com/PKnYF5V.png)

### Restricted Chaos Games
Modify the game such that current vertex is removed from the random draw of the next vertex.

Let n = 4 and step = 1/2.

```python
h = CANVAS_WIDTH / 2
k = CANVAS_HEIGHT / 2
P = polygons.Polygon(h, k, 200, 4)
C = chaos_game.chaos_game_2(P, 1/2, 100000)
draw.draw_list(C, canvas, color=draw.RED)
```
![Restricted chaos game](https://i.imgur.com/3HEK9C0.png)

cast = True
```python
h = CANVAS_WIDTH / 2
k = CANVAS_HEIGHT / 2
P = polygons.Polygon(h, k, 200, 4)
C = chaos_game.chaos_game_2(P, 1/2, 100000, cast=True)
draw.draw_list(C, canvas, color=draw.RED)
```
![Restricted chaos game](https://i.imgur.com/qAGGOvm.png)

----

Let n = 6 and step = 2/3.

```python
h = CANVAS_WIDTH / 2
k = CANVAS_HEIGHT / 2
P = polygons.Polygon(h, k, 200, 6)
C = chaos_game.chaos_game_2(P, 2/3, 100000)
draw.draw_list(C, canvas, color=draw.GREEN)
```
![Restricted chaos game](https://i.imgur.com/TWSqthk.png)

----

Change the game such that the random index of the next vertex must strictly be greater than the previous (or wrap around).

Let n = 4 and step = 1/2.

```python
h = CANVAS_WIDTH / 2
k = CANVAS_HEIGHT / 2
P = polygons.Polygon(h, k, 200, 4)
C = chaos_game.chaos_game_3(P, 1/2, 100000)
draw.draw_list(C, canvas, color=draw.BLUE)
```
![Restricted chaos game](https://i.imgur.com/auRYyU4.png)

cast = True

```python
h = CANVAS_WIDTH / 2
k = CANVAS_HEIGHT / 2
P = polygons.Polygon(h, k, 200, 4)
C = chaos_game.chaos_game_3(P, 1/2, 100000, cast=True)
draw.draw_list(C, canvas, color=draw.VIOLET)
```
![Restricted chaos game](https://i.imgur.com/cyTv26C.png)

## Barnsley Fern
[source](https://en.wikipedia.org/wiki/Barnsley_fern)

```python
fern = chaos_game.barnsley_fern(100000)
draw.draw_list(fern, canvas, color=draw.MAGENTA)
```
![Barnsley fern](https://i.imgur.com/Gi0m47g.png)


## Grid Visualizations

### boiler plate
```python
import itertools
import pygame
import chaos_game
import polygons
import draw

pygame.init()

CANVAS_WIDTH = 1800
CANVAS_HEIGHT = 1000
canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
canvas.fill(draw.BASE03)

# code here

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
```

### Polygon Grid
4 by 3 grid of polygons where n is incremented by 1
```python
rows = 3
cols = 4
info = draw.grid_info(CANVAS_WIDTH, CANVAS_HEIGHT, cols, rows)
polys = [polygons.Polygon(h, k, info['radius'], n) for (h, k), n in zip(info['centers'], itertools.count(3))]
for p in polys:
    pygame.draw.polygon(canvas, draw.WHITE, p.vertices)

# text labels
pygame.font.init()
myfont = pygame.font.Font(pygame.font.get_default_font(), 30)
for (x, y), n in zip(info['centers'], itertools.count(3)):
    text = myfont.render(f'{n}-gon', True, draw.BASE03)
    canvas.blit(text, dest=(x, y))
```
![Polygons](https://i.imgur.com/NiGbowm.png)

### Chaos Game Grid
4 by 3 grid of chaos games where step = 1/2 and n = 10000 on the previous set of polygons
```python
rows = 3
cols = 4
info = draw.grid_info(CANVAS_WIDTH, CANVAS_HEIGHT, cols, rows)
polys = [polygons.Polygon(h, k, info['radius'], n) for (h, k), n in zip(info['centers'], itertools.count(3))]
draw.draw_lists([chaos_game.chaos_game(p, 1/2, 10000) for p in polys], canvas, color=draw.ORANGE)

# text labels
pygame.font.init()
myfont = pygame.font.Font(pygame.font.get_default_font(), 30)
for n, (x, y) in zip(itertools.cycle(range(3, 7)), info['centers']):
    text = myfont.render(f'{n}-gon', True, draw.BASE0)
    y = y + 100
    x = x + 100
    canvas.blit(text, dest=(int(x), int(y)))
```
![Chaos games](https://i.imgur.com/uqfCKMt.png)
----
Several chaos game variations at once
```python
rows = 3
cols = 4
info = draw.grid_info(CANVAS_WIDTH, CANVAS_HEIGHT, cols, rows)
polys = [polygons.Polygon(h, k, info['radius'], n) for (h, k), n in zip(info['centers'], itertools.cycle(range(3, 3 + cols)))]
draw.draw_lists([chaos_game.chaos_game(p, 1/2, 10000) for p in polys[0:4]], canvas, color=draw.CYAN)
draw.draw_lists([chaos_game.chaos_game_2(p, 1/2, 10000) for p in polys[4:8]], canvas, color=draw.YELLOW)
draw.draw_lists([chaos_game.chaos_game_3(p, 1/2, 10000) for p in polys[8:12]], canvas, color=draw.VIOLET)

# text labels
pygame.font.init()
myfont = pygame.font.Font(pygame.font.get_default_font(), 30)
delta_x = CANVAS_WIDTH / (cols)
delta_y = CANVAS_HEIGHT / (rows)
offset_x = delta_x / 2
offset_y = delta_y / 2
for n, color in zip(range(3), [draw.CYAN, draw.YELLOW, draw.VIOLET]):
    text = myfont.render(f'variant: {n + 1}', True, color)
    x = 10
    y = (delta_y * n) + (offset_y / 2)
    canvas.blit(text, dest=(x, int(y)))

for n, (x, y) in zip(itertools.cycle(range(3, 7)), info['centers']):
    text = myfont.render(f'{n}-gon', True, draw.BASE0)
    y = y + 100
    x = x + 100
    canvas.blit(text, dest=(int(x), int(y)))
```
![Several chaos games](https://i.imgur.com/WWD8H9B.png)
