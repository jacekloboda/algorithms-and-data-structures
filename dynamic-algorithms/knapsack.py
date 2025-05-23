# knapsack problem

# iterative approach
def knapsack(P, W, k):  # P - list of prices, W - list of weights, k - backpack weight capacity

    n = len(P)
    F = [[0]*(k+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, k+1):
            F[i][j] = F[i-1][j]

            if 0 <= j-W[i-1]:
                F[i][j] = max(F[i][j], F[i-1][j-W[i-1]]+P[i-1])

    return F[n][k]


# recursive approach
D = {}


def knapsack2(P, W, i, k):

    if k == 0:
        return 0
    if i == 0:
        return 0

    if (i, k) in D:
        return D[(i, k)]

    val = knapsack2(P, W, i-1, k)

    if 0 <= k-W[i]:
        val = max(val, knapsack2(P, W, i-1, k-W[i])+P[i])

    D[(i, k)] = val
    return val
