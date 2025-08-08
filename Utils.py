from Particula import Particula
import random

def get_indexes_to_check(i, j):
    res = []
    res.append([i,j])
    res.append([i-1, j+1])
    res.append([i, j+1])
    res.append([i+1, j+1])
    res.append([i+1, j])
    return res

def cell_index_method(particulas: list[Particula], N, L, M, r_c):
    cell = [[[] for _ in range(M)] for _ in range(M)]
    l = L / M
    for k in range(0, N):
        particula = particulas[k]
        particula.set_ind(k)
        i = int(particula.y // l)
        j = int(particula.x // l)
        cell[i][j].append(particula)
    res = [[-1 for _ in range(N)] for _ in range(N)]
    for k in range(0, N):
        particula = particulas[k]
        i_p = int(particula.y // l)
        j_p = int(particula.x // l)
        indexes = get_indexes_to_check(i_p, j_p)
        for index in indexes:
            i = index[0]
            j = index[1]
            if i < 0 or j < 0 or i >= M or j >= M:
                continue
            for p in cell[i][j]:
                dist = particula.dist(p)
                if dist <= r_c:
                    res[particula.ind][p.ind] = dist
                    res[p.ind][particula.ind] = dist
    # @TODO: agarrar la matriz y devolver la lista con las particulas en ese radio de interaccion
    return res

def exists_particle(particle, particles):
    for p in particles:
        if p.dist(particle) <= 0:
            return True
    return False

def generate_random_particles(N, L, r):
    res = []
    for _ in range(0, N):
        x = random.randint(r, L - r)
        y = random.randint(r, L - r)
        p = Particula(x, y, r)
        while(exists_particle(p, res)):
            x = random.randint(r, L - r)
            y = random.randint(r, L - r)
            p = Particula(x, y, r)
        res.append(p)
    return res

part = generate_random_particles(3, 10, 2)
for p in part:
    print(p)

dists = cell_index_method(part, 3, 40, 4, 2)
print(dists)