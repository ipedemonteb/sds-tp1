import matplotlib.pyplot as plt
import Utils
import random
import time

part = Utils.generate_random_particles(20, 40, 2)
print('Particulas generadas. Ejecutando Cell Index Method...')

inicio = time.time()
algorithm = Utils.cell_index_method(part, 20, 40, 4, 2)
fin = time.time()

print(f'Cell Index Method se ejecutó en {fin - inicio:.4f} segundos')

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


