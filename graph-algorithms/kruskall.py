class Node:

    def __init__(self):

        self.paret = self
        self.rank = 0


def find(x):

    if x != x.parent:

        x.parent = find(x.parent)

    return x.parent


def union(x, y):

    x = find(x)
    y = find(y)

    if x.rank < y.rank:

        x.parent = y

    else:

        y.parent = x

        if x.rank == y.rank:

            x.rank += 1


def kruskall(G):  # find and return MST of G

    n = len(G)
    E = []

    for u in range(n):
        for v, wgt in G[u]:

            if u < v:
                E.append((u, v, wgt))

    N = [Node() for _ in range(n)]
    MST = []
    MST_sum = 0

    for u, v, wgt in sorted(E, key=lambda x: x[2]):

        if find(N[u]) != find(N[v]):

            union(N[u], N[v])
            MST.append((u, v, wgt))
            MST_sum += wgt

    return MST, MST_sum
