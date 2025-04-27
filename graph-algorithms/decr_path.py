# path with decreasing edge weights, using dfs and list of visited edges

def derc_path(G, s, t):

    n = len(G)
    E_vis = []
    Path = []

    ind = 0

    for u in range(n):

        for i in range(len(G[u])):

            wgt, v = G[u][i]
            G[u][i] = (wgt, v, ind)
            E_vis.append(False)
            ind += 1

    def dfs_visit(G, u, last_wgt):

        nonlocal Path
        nonlocal E_vis

        Path.append(u)

        if u == t:
            return True

        if len(G[u]) == 0:

            return False

        for wgt, v, ind in G[u]:

            if wgt < last_wgt and not E_vis[ind]:

                E_vis[ind] = True
                if dfs_visit(G, v, wgt):
                    return True

                E_vis[ind] = False

        Path.pop()

        return False

    dfs_visit(G, s, float('inf'))

    return Path if Path and Path[-1] == t else []


G = [[(4, 1), (1, 4)],
     [],
     [],
     [(2, 3)],
     [(1, 3)]
     ]

print(derc_path(G, 0, 3))
