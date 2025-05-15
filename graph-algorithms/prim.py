# implementation of prim's algorithms in python

def prim(G, s):  # G - list of adj, starting node

    from queue import PriorityQueue

    n = len(G)
    P = [-1]*n
    D = [float('inf')]*n
    D[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty():

        dist, u = Q.get()

        if D[u] < dist:
            continue

        for v, wgt in G[u]:
            if wgt < D[v]:

                D[v] = wgt
                P[v] = u
                Q.put((D[v], v))

    return P
