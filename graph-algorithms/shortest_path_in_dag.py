# weighted dag (including negative weights)
# find shortest path from s to every node

# topologic sort
# then relaxing  in sorted order
# linear time complex O(E+V)

# G list of neighborhood (neighbor, weight)

def shortest_path(G, s):

    def topologic_sort(G, s):

        n = len(G)
        V = [False for _ in range(n)]
        Sorted_nodes = []

        def dfs_visit(G, u):

            V[u] = True

            for v in G[u]:

                if not V[v]:

                    dfs_visit(G, v)

            Sorted_nodes.append(u)

        for u in range(n):

            if not V[u]:

                dfs_visit(G, u)

        return Sorted_nodes[::-1]

    n = len(G)
    Nodes = topologic_sort(G, s)
    D = [float('inf') for _ in range(n)]
    D[s] = 0

    for u in Nodes:

        for v, w in G[u]:

            if D[v] > D[u] + w:

                D[v] = D[u] + w

    return D
