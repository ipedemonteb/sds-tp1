import matplotlib.pyplot as plt
import Utils
import random

part = Utils.generate_random_particles(20, 40, 2)
print('Particulas generadas')
algorithm = Utils.cell_index_method(part, 20, 40, 4, 2)
print('Algoritmo ejecutado')

x = [p.x for p in part]
y = [p.y for p in part]
colors = ["red" for _ in part]
rand = random.randint(0, 19)
colors[rand] = "green"
for p in algorithm[rand]:
    colors[p.ind] = "blue"

plt.scatter(x, y, c=colors, s=100)

plt.title("Gráfico de puntos")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)

plt.show()


