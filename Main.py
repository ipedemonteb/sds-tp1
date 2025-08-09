import matplotlib.pyplot as plt
import Utils
import random
import time

N = int(input("Ingrese N, la cantidad de particulas: "))
L = float(input("Ingrese L, la longitud de la grilla: "))
r_c = float(input("Ingrese r_c, el radio de interacción: "))
r = float(input("Ingrese r, el radio de las partículas: "))
M = int(input(f'Ingrese M, donde MxM es la cantidad de celdas de la grilla (menor o igual a {int(L / (r_c + 2*r))}): '))

part = Utils.generate_random_particles(N, L, r)
print('Particulas generadas. Ejecutando Cell Index Method...')

inicio = time.time()
algorithm = Utils.cell_index_method(part, N, L, M, r_c)
fin = time.time()

print(f'Cell Index Method se ejecutó en {fin - inicio:.4f} segundos')

x = [p.x for p in part]
y = [p.y for p in part]
colors = ["red" for _ in part]
rand = random.randint(0, N-1)
colors[rand] = "green"
for p in algorithm[rand]:
    colors[p.ind] = "blue"

plt.scatter(x, y, c=colors, s=50)

plt.title("Gráfico de puntos")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)

plt.show()
