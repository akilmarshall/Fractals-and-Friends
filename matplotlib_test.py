from chaos_game import polygons, chaos_game
import matplotlib.pyplot as plt


h, k = 0, 0
p = polygons.Polygon(h, k, 2000, 4)
c = chaos_game.chaos_game_3(p, 1/2, 1000)
x, y = zip(*c)
plt.scatter(x, y)
plt.show()
