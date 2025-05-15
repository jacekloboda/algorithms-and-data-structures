# longest increasing subsequence

def lis(A):

    n = len(A)
    F = [1]*n
    P = [-1]*n
    max_ind = 0

    for i in range(1, n):
        for j in range(i):

            if A[j] < A[i] and F[i] < F[j]+1:
                F[i] = F[j]+1
                max_ind = i
                P[i] = j

    return F[max_ind], P
