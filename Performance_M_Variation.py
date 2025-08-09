import matplotlib.pyplot as plt
import Utils
import time

# L / M > r_c + 2r => M < L / (r_c + 2r)

N = 500
L = 20
r_c = 1
r = 0.25
M_max = int(L / (r_c + 2*r))
print(f'N = {N}, L = {L}, r_c = {r_c}, r = {r} => M <= {M_max}')
part = Utils.generate_random_particles(N, L, r)
print('Particulas generadas. Probando distintos valores de M.')

cell_index_method_graph = []

m_values = range(1, M_max+1)
for M in m_values:
    print('=======')
    print(f'M = {M}')
    print('-------')
    print('Midiendo el tiempo con Cell Index Method')
    inicio = time.time()
    Utils.cell_index_method(part, N, L, M, r_c)
    fin = time.time()
    cell_index_method_graph.append(fin - inicio)
    print(f'Cell Index Method se ejecutó en {fin - inicio:.4f} segundos')

plt.plot(m_values, cell_index_method_graph, marker='o', label="Cell Index Method")
plt.xlabel("M")
plt.ylabel("Tiempo de ejecucion")
plt.grid(True)
plt.legend()

plt.show()
