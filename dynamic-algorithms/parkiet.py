# Jacek Loboda
# dynamic approach
# tablice nxm wypelniam w ten sposob: F[i][j] to minimalna ilosc ciec potrzebnych do uzyskania blatu ktorego lewy gorny naroznik to (i, j)
# jesli danego naroznika nie da sie uzyskac bo np trzeba by odciac deske z liczba sekow > s to zostawiam tam inf
# na koniec przechodze po kolumnie m-1 i wierszu n-1 talicy F i znajduje najmniejsze
# pole ktore bedac ostatnia deska mialoby liczbe sekow <= s
# zlozonosc czasowa: O(nm)
# greedy approach
# rozwazam dwa podejscia
# 1) tne lewa krawedz jak najczesniej, tne gorna tylko jak nie moge lewej
# 2) analogicznie tylko tne gorna krawedz jak najczesciej
# zwracam mniejsza liczbe ciec z obu podejsc


def parkiet_dp(B, C, s):

    n = len(B)
    m = len(B[0])
    F = [[float('inf')]*m for _ in range(n)]

    F[0][0] = 0

    for i in range(n):
        for j in range(m):

            if i > 0 and C[i-1][j]-C[i][j] <= s:
                F[i][j] = min(F[i][j], F[i-1][j]+1)

            if j > 0 and C[i][j-1]-C[i][j] <= s:
                F[i][j] = min(F[i][j], F[i][j-1]+1)

    res = F[n-1][m-1]
    for i in range(n-1):
        if C[i][m-1] <= s:
            res = min(res, F[i][m-1])

    for j in range(m-1):
        if C[n-1][j] <= s:
            res = min(res, F[n-1][j])

    return -1 if res == float('inf') else res


def parkiet_greedy(B, C, s):

    n = len(B)
    m = len(B[0])

    i = 0
    j = 0

    res1 = float('inf')

    while i < n or j < m:
        if (i == n-1 or j == m-1) and C[i][j] <= s:
            res1 = i+j
            break

        if i < n-1 and C[i][j]-C[i+1][j] <= s:
            i += 1
            continue

        if j < m-1 and C[i][j]-C[i][j+1] <= s:
            j += 1
            continue

        break

    i = 0
    j = 0
    res2 = float('inf')
    while i < n or j < m:
        if (i == n-1 or j == m-1) and C[i][j] <= s:
            res2 = i+j
            break

        if j < m-1 and C[i][j]-C[i][j+1] <= s:
            j += 1
            continue

        if i < n-1 and C[i][j]-C[i+1][j] <= s:
            i += 1
            continue

        break

    res1 = min(res1, res2)

    return -1 if res1 == float('inf') else res1
