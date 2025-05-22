# coin change making porblem
# A - list of coins, k - change

# v1:
# coins in A are one use only
def f1(A, k):

    M = [0]
    M.extend(A)
    n = len(M)
    F = [[float('inf')]*(k+1) for _ in range(n)]

    for i in range(1, n):
        F[i][0] = 0

    for i in range(1, k+1):
        F[0][i] = float('inf')

    for i in range(1, n):
        for j in range(1, k+1):
            F[i][j] = F[i-1][j]

            if 0 <= j-M[i]:
                F[i][j] = min(F[i][j], F[i-1][j-M[i]]+1)

    return F[n-1][k]

# v2
# coins in A can be used multiple times


def f2(A, k):

    M = [0]
    M.extend(A)
    n = len(M)
    F = [[float('inf')]*(k+1) for _ in range(n)]

    for i in range(1, n):
        F[i][0] = 0

    for i in range(1, k+1):
        F[0][i] = float('inf')

    for i in range(1, n):
        for j in range(1, k+1):
            F[i][j] = F[i-1][j]

            a = 1

            while 0 <= j-a*M[i]:
                F[i][j] = min(F[i][j], F[i-1][j-a*M[i]]+a)
                a += 1

    for row in F:
        print(row)

    return F[n-1][k]


A = [2, 3, 5, 10]

print(f2(A, 9))
