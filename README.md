# Fractals and Friends
 A repository for my exploration and research of fractals and kindred self similar processes/structures. Pygame will be used to create graphics and animations.
## Todo
- [ ] Convert api to object oriented
- [ ] Add functional option to api
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

To match the Wikipedia picture for regular polygons where n = 4 set phi = pi / 4

### Sierpinski Triangle
![Sierpinski triangle](https://i.imgur.com/9rqMZRx.png)
```python
pixels = pygame.PixelArray(canvas)                       
P = chaos_game.regular_polygon((canvas_width / 2, canvas_height / 2), 3, 200)
C = chaos_game.chaos_game(P, 1/2, 100000)                
chaos_game.draw_chaos_game(C, pixels, color=blue)
```

----

Let n = 6 and step = 2/3.

![Chaos game](https://i.imgur.com/GySZ2wn.png)

```python
pixels = pygame.PixelArray(canvas)                       
P = chaos_game.regular_polygon((canvas_width / 2, canvas_height / 2), 6, 200)
C = chaos_game.chaos_game(P, 2/3, 100000)                
chaos_game.draw_chaos_game(C, pixels, color=yellow)
```

### Restricted Chaos Games
Modify the game such that current vertex is removed from the random draw of the next vertex. N = 4, step = 1/2.

![Restricted chaos game](https://i.imgur.com/xgvsM2o.png)
```python
pixels = pygame.PixelArray(canvas)                       
P = chaos_game.regular_polygon((canvas_width / 2, canvas_height / 2), 4, 200)
C = chaos_game.restricted_chaos_game(P, 1/2, 100000)                
chaos_game.draw_chaos_game(C, pixels, color=red)
```

n = 6, step = 2/3

![Restricted](https://i.imgur.com/C9fxG7g.png)

```python
pixels = pygame.PixelArray(canvas)                       
P = chaos_game.regular_polygon((canvas_width / 2, canvas_height / 2), 6, 200)
C = chaos_game.restricted_chaos_game(P, 2/3, 100000)                
chaos_game.draw_chaos_game(C, pixels, color=green)
```

----

Change the game such that the random index of the next vertex must strictly be greater than the previous (or wrap around).

Let n = 4 and step = 1/2

![Restriced chaos game](https://i.imgur.com/wc8jZca.png)

```python
pixels = pygame.PixelArray(canvas)                       
P = chaos_game.regular_polygon((canvas_width / 2, canvas_height / 2), 4, 200)
C = chaos_game.restricted_chaos_game_2(P, 2/3, 100000)                
chaos_game.draw_chaos_game(C, pixels, color=violet)
```

## Barnsley Fern
[source](https://en.wikipedia.org/wiki/Barnsley_fern)
```python
pixels = pygame.PixelArray(canvas)
B = barnsley_fern(10000)
draw_chaos_game(B, pixels)
```
![Barnsley fern](https://i.imgur.com/8oPOKlJ.png)
