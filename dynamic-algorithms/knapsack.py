# knapsack problem

def knapsack(P, W, k):  # P - list of prices, W - list of weights, k - backpack weight capacity

    n = len(P)
    F = [[0]*(k+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, k+1):
            F[i][j] = F[i-1][j]

            if 0 <= j-W[i-1]:
                F[i][j] = max(F[i][j], F[i-1][j-W[i-1]]+P[i-1])

    return F[n][k]
