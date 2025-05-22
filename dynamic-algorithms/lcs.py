# lcs - longest common subsequence

def lcs(s1, s2):
    s1 = 'a'+s1
    s2 = 'a'+s2
    n = len(s1)
    m = len(s2)
    F = [[0]*(n) for _ in range(m)]

    for i in range(1, n):
        for j in range(1, m):
            if s1[i] == s2[j]:
                F[i][j] = F[i-1][j-1]+1
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])

    return F[n][m]
