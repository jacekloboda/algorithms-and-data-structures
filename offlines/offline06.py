# Szalony Inwestor wybudował po południowej stronie drogi n biurowców, na pozycjach x0 < ⋯ < xn−1.
# Parkingi tych biurowców mają dopiero zostać wybudowane i dostępne jest w tym celu m działek (m ≥ n),
# dostępnych na północnej stronie drogi, na pozycjach y0 < ⋯ < ym−1.
# Inwestor chce wybudować dokładnie po jednym parkingu dla każdego biurowca (żadne dwa biurowce nie
# mogą dzielić tego samego parkingu). Zasady bezpiecznego ruchu wymagają, że i-ty biurowiec musi
# mieć parking na pozycji wcześniejszej niż i + 1-szy. Inwestor chce wybudować parkingi na takich
# pozycjach, żeby suma odległości parkingów od biurowców była minimalna. Odległość i-go biurowca
# od j-ej działki to ∣xi − yj ∣. Zadanie polega na implementacji funkcji:
# parking( X, Y )
# która na wejściu otrzymuje listę X zawierającą n pozycji biurowców oraz listę Y zawierającą m
# pozycji działek na parkingi (listy X oraz Y zawierają nieujemne liczby całkowite). Funkcja powinna
# być możliwie jak najszybsza.
#
# zlozonosc: O(mn)
#
# opis: funkcja parking iteracyjnie wypelnia tablice n x m elementow F[i][j] jest najmniejsza mozliwa suma odleglosci wszytskich kombinacji budynkow od 0 do i i parkingow od 0 do j


def parking(X, Y):

    def dist(x, y):
        return abs(X[x]-Y[y])

    n = len(X)
    m = len(Y)

    F = [[float('inf')]*m for _ in range(n)]

    min_val = float('inf')
    for j in range(m):
        min_val = min(min_val, dist(0, j))
        F[0][j] = min_val

    for i in range(1, n):
        for j in range(m):
            if j < i:
                F[i][j] = float('inf')

            else:
                F[i][j] = F[i-1][j-1] + dist(i, j)
                F[i][j] = min(F[i][j], F[i][j-1])

    return F[n-1][m-1]
