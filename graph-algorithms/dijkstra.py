# implementaion of Dijkstra algorithm in python

# using list of neighborhoods

def disjktra(G, s):  # G - list of neighbors with weight of edge (weight, neighbor), s - starting node

    import heapq

    n = len(G)
    D = [float('inf') for _ in range(n)]
    D[s] = 0
    Q = [(0, s)]

    while Q:

        dist, u = heapq.heappop(Q)

        if dist > D[u]:
            continue

        for w, v in G[u]:

            if D[u] + w < D[v]:

                D[v] = D[u] + w
                heapq.heappush(Q, (D[v], v))

    return D

# using matrix of edges


def dijksrta(W, s):  # W list of edges with weights, s starting node

    n = len(W)
    # distance of every node from s, inf if not connected
    D = [float('inf') for _ in range(n)]
    V = [False for _ in range(n)]  # visited status for every node

    D[s] = 0
    V[s] = False

    for _ in range(n):

        min_d = float('inf')
        k = -1

        for u in range(n):

            if not V[u] and min_d < D[u]:

                min_d = D[u]
                k = u

        V[k] = True

        for u in range(n):

            if D[u] > D[k] + W[k][u]:

                D[u] = D[k] + W[k][u]

    return D
