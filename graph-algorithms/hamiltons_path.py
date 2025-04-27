# dag, find hamilton's path
# using topologic sorting
# in sorted nodes there must be edge from every i-th node to (i+1)th

def topological_sort(G):

    n = len(G)
    V = [False] * n
    Sorted_nodes = []

    def dfs_visit(G, u):

        nonlocal V
        nonlocal Sorted_nodes

        V[u] = True

        for v in G[u]:

            if not V[v]:

                dfs_visit(G, v)

        Sorted_nodes.append(u)

    for u in range(n):

        if not V[u]:

            dfs_visit(G, u)

    return Sorted_nodes[::-1]


def hamiltons_path(G):

    Nodes = topological_sort(G)
    n = len(Nodes)

    for i in range(1, n):

        flag = False

        for v in G[Nodes[i-1]]:

            if v == Nodes[i]:
                flag = True

        if not flag:
            return []  # there is no path

    return Nodes
