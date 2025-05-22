# sum of subsequence
# does A contain subsequence with sum is equal to k, return True of False

def f(A, k):
    n = len(A)
    F = [[False]*(k+1) for _ in range(n)]

    for i in range(n):
        F[i][0] = True

    for i in range(n):
        for j in range(k+1):
            F[i][j] = F[i-1][j]

            if 0 <= j-A[i]:
                F[i][j] = F[i][j] or F[i-1][j-A[i]]

    return F[n-1][k]
