import matplotlib.pyplot as plt
import Utils
import time

L = 20
r_c = 1
r = 0.25
M_max = int(L / (r_c + 2*r))
periodic = int(input('Ingrese si desea ejecutar con condiciones periodicas de contorno (1 = SI, 0 = NO): '))
print(f'L = {L}, r_c = {r_c}, r = {r} => M fijo en {M_max}')

cell_index_method_graph = []
brute_force_graph = []
n_values = range(200, 401, 10)

for N in n_values:
    print('=======')
    print(f'N = {N}')
    print('-------')

    part = Utils.generate_random_particles(N, L, r)
    print('Midiendo el tiempo con Cell Index Method')
    inicio = time.time()
    Utils.cell_index_method(part, N, L, M_max, r_c, periodic)
    fin = time.time()
    tiempo = fin - inicio
    cell_index_method_graph.append(tiempo)
    print(f'Cell Index Method se ejecutó en {tiempo:.4f} segundos')

    print('Ahora midiendo el tiempo con Fuerza Bruta')
    inicio2 = time.time()
    Utils.brute_force(part, N, L, r_c, periodic)
    fin2 = time.time()
    tiempo2 = fin2 - inicio2
    brute_force_graph.append(tiempo2)
    print(f'Fuerza Bruta se ejecutó en {tiempo2:.4f} segundos')

plt.plot(n_values, cell_index_method_graph, marker='o', label=f"Cell Index Method")
plt.plot(n_values, brute_force_graph, marker='o', label=f"Fuerza Bruta")
plt.xlabel("N")
plt.ylabel("Tiempo de ejecucion (s)")
plt.grid(True)
plt.legend()
plt.show()
