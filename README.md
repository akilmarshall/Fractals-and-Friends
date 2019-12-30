# Fractals and Friends
 A framework for my exploration and research of fractals and kindred self similar processes/structures. written in python with heavy usage of [pygame](https://www.pygame.org/wiki/about)

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

## Boilerplate
```python
import pygame
import chaos_game

pygame.init()

black = (0, 0, 0)
blue = (38, 139, 210)
yellow  (181, 137, 0)
red = (220, 50, 47)
green = (153, 0, 68)
magenta = (211, 54, 130)

canvas_width = 500
canvas_height = 500
canvas = pygame.display.set_mode((canvas_width, canvas_height))
canvas.fill(black)

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
pixels = pygame.PixelArray(canvas)                       
P = chaos_game.regular_polygon((canvas_width / 2, canvas_height / 2), 3, 200)
C = chaos_game.chaos_game(P, 1/2, 100000)                
chaos_game.draw_chaos_game(C, pixels, color=blue)
```
![Sierpinski triangle](https://i.imgur.com/9rqMZRx.png)

----

Let n = 6 and step = 2/3.

```python
pixels = pygame.PixelArray(canvas)                       
P = chaos_game.regular_polygon((canvas_width / 2, canvas_height / 2), 6, 200)
C = chaos_game.chaos_game(P, 2/3, 100000)                
chaos_game.draw_chaos_game(C, pixels, color=yellow)
```
![Chaos game](https://i.imgur.com/GySZ2wn.png)

### Restricted Chaos Games
Modify the game such that current vertex is removed from the random draw of the next vertex.

Let n = 4 and step = 1/2.

```python
pixels = pygame.PixelArray(canvas)                       
P = chaos_game.regular_polygon((canvas_width / 2, canvas_height / 2), 4, 200)
C = chaos_game.restricted_chaos_game(P, 1/2, 100000)                
chaos_game.draw_chaos_game(C, pixels, color=red)
```
![Restricted chaos game](https://i.imgur.com/xgvsM2o.png)

----

Let n = 6 and step = 2/3.

```python
pixels = pygame.PixelArray(canvas)                       
P = chaos_game.regular_polygon((canvas_width / 2, canvas_height / 2), 6, 200)
C = chaos_game.restricted_chaos_game(P, 2/3, 100000)                
chaos_game.draw_chaos_game(C, pixels, color=green)
```
![Restricted chaos game](https://i.imgur.com/C9fxG7g.png)

----

Change the game such that the random index of the next vertex must strictly be greater than the previous (or wrap around).

Let n = 4 and step = 1/2.

```python
pixels = pygame.PixelArray(canvas)                       
P = chaos_game.regular_polygon((canvas_width / 2, canvas_height / 2), 4, 200)
C = chaos_game.restricted_chaos_game_2(P, 2/3, 100000)                
chaos_game.draw_chaos_game(C, pixels, color=violet)
```
![Restriced chaos game](https://i.imgur.com/wc8jZca.png)

## Barnsley Fern
[source](https://en.wikipedia.org/wiki/Barnsley_fern)

```python
pixels = pygame.PixelArray(canvas)
B = barnsley_fern(10000)
draw_chaos_game(B, pixels)
```
![Barnsley fern](https://i.imgur.com/8oPOKlJ.png)

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
