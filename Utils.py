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
    res = [[] for _ in range(N)]
    dist = [[-1 for _ in range(N)] for _ in range(N)]
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
                d = particula.dist(p)
                if p != particula and dist[particula.ind][p.ind] < 0 and d <= r_c:
                    dist[particula.ind][p.ind] = d
                    dist[p.ind][particula.ind] = d
                    res[particula.ind].append(particulas[p.ind])
                    res[p.ind].append(particulas[particula.ind])
    return res

def brute_force(particulas: list[Particula], N, r_c):
    res = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and particulas[i].dist(particulas[j]) <= r_c:
                res[i].append(particulas[j])
    return res

def exists_particle(particle, particles):
    for p in particles:
        if p.dist(particle) <= 0:
            return True
    return False

def generate_random_particles(N, L, r):
    res = []
    for _ in range(0, N):
        x = random.uniform(r, L - r)
        y = random.uniform(r, L - r)
        p = Particula(x, y, r)
        while(exists_particle(p, res)):
            x = random.uniform(r, L - r)
            y = random.uniform(r, L - r)
            p = Particula(x, y, r)
        res.append(p)
    return res
