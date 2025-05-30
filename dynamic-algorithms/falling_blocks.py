# spadajace klocki
# lis z innym kryterium
# T - lista klockow T[i] = (poczatek, koniec) jako koordynaty

# rozwiazanie iteracyjne
def solve(T):

    n = len(T)
    F = [1]*n  # longest tower ending on i-th block
    P = [-1]*n  # parents in tower

    for i in range(1, n):
        for j in range(i):
            if (T[j][0] <= T[i][0] and T[i][1] <= T[j][1]) and F[i] < F[j]+1:
                F[i] = F[j]+1
                P[i] = j

    max_ind = 0
    for i in range(n):
        if F[i] > F[max_ind]:
            max_ind = i

    return F[max_ind], P
