import Utils

N = 500
L = 20
r_c = 1
r = 0.25
M = 13

part = Utils.generate_random_particles(N, L, r)
cell_index_method = Utils.cell_index_method(part, N, L, M, r_c)
brute_force = Utils.brute_force(part, N, r_c)

for i in range(0, N):
    q = len(cell_index_method[i])
    cell_index_method[i].sort(key=lambda p : (p.x, p.y, p.r))
    brute_force[i].sort(key=lambda p : (p.x, p.y, p.r))
    for j in range(0, q):
        assert(cell_index_method[i][j] == brute_force[i][j])
print('OK')
