import heapq

import numpy as np
from scipy.optimize import linear_sum_assignment

def dfs(t):
    yield t
    for c in t[1]:
        yield from dfs(c)

def tree_size(t):
    return len(list(dfs(t)))

def sc(a, b, x, y):
    if a == 0 or b == 0:
        return 1
    elif x[a-1][0] == y[b-1][0]:
        return 0
    else:
        return 0.8

def c(M, x, y):
    s = 0
    for m in M:
        if 0 in m:
            s += 1
        elif x[m[0]-1][0] != y[m[1]-1][0]:
            s += 0.8
    return s

def heuristic(m, n, x, y):
    len_m = len(m)
    len_n = len(n)

    if len_m == 0:
        return len_n
    if len_n == 0:
        return len_m

    cm = np.ones((len_m + 1, len_n + 1), dtype=float)
    cm[-1, -1] = 0

    for i, mi in enumerate(m):
        for j, nj in enumerate(n):
            cm[i, j] = sc(mi, nj, x, y)

    row_ind, col_ind = linear_sum_assignment(cm)
    return cm[row_ind, col_ind].sum()

def I(M):
    return {x[0] for x in M}

def J(M):
    return {x[1] for x in M}

def descendants(e, x):
    d = set()
    for c in x[e-1][1]:
        d.add(x.index(c) + 1)
        d.update(descendants(x.index(c) + 1, x))
    return d

def get_parent(e, t):
    for x in dfs(t):
        for c in x[1]:
            if c == e:
                return x

def get_map(i, m, s):
    for x in m:
        if x[s] == i:
            return x
def get_index(e, x):
    for i in range(len(x)):
        if x[i] == e:
            return i + 1

def largest_ancestor(i, M, pm):
    p = pm[i-1]
    m = get_map(p, M, 0)
    if m[1] != 0:
        return m
    return largest_ancestor(p, M, pm)

def ancestor_path(s, p, pm2):
    path = []
    while True:
        n = pm2[s-1]
        if n is None:
            break
        if n == p:
            break
        path.append(n)
        s = n
    return path


def compute_cache(t1):
    x = list(dfs(t1))
    dx = [descendants(q, x) for q in range(1, len(x) + 1)]
    pm1 = [get_index(get_parent(q, t1), x) for q in x]
    return x, dx, pm1

def u_ted(t1, t2, cache=None):

    hm = {}

    def h(m, n, x, y):
        ky = (frozenset(m), frozenset(n))
        if ky not in hm:
            hm[ky] = heuristic(m, n, x, y)
        return hm[ky]

    t1 = (0, [t1])
    t2 = (0, [t2])

    if cache is None:
        x, dx, pm1 = compute_cache(t1)
        y, dy, pm2 = compute_cache(t2)
    else:
        x, dx, pm1, y, dy, pm2 = cache

    M = {(1, 1)}
    Q = [(c(M, x, y) + h(set(range(1, len(x) + 1)), set(range(1, len(y) + 1)), x, y), M)]

    while Q:
        ch, M = heapq.heappop(Q)
        i = min(set(range(1, len(x) + 2)) - I(M))

        if i == len(x) + 1:
            fm = M.union({(0, j) for j in set(range(1, len(y) + 1)) - J(M)})
            return c(fm, x, y), fm

        k, l = largest_ancestor(i, M, pm1)

        hp = h(set(range(1, len(x) + 1)) - dx[k-1].union(I(M)), set(range(1, len(y) + 1)) - dy[l-1].union(J(M)), x, y)

        M0 = M.union({(i, 0)})
        h0 = h(dx[k-1] - I(M0), dy[l-1] - J(M0), x, y) + hp
        nm = [(M0, h0)]

        for j in dy[l-1] - J(M):
            path = [p for p in ancestor_path(j, l, pm2)]
            Mj = M.union({(i, j)}.union({(0, q) for q in path}))
            hj = h(dx[i-1] - I(Mj), dy[j-1] - J(Mj), x, y) + h(dx[k-1] - dx[i-1].union(I(Mj)), dy[l-1] - dy[j-1].union(J(Mj)), x, y) + hp
            nm.append((Mj, hj))

        for mn, hn in nm:
            heapq.heappush(Q, (c(mn, x, y) + hn, mn))

def u_sim(t1, t2, cache=None):
    max_size = max(tree_size(t1), tree_size(t2))
    if max_size == 0:
        return 1.0

    dist, _ = u_ted(t1, t2, cache)

    return 1 - dist / max_size