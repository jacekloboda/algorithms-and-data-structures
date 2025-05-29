# find cheapest path for king from [0][0] to [n-1][n-1]
# A - chessboard nxn, with cost on each tile

# recursive aproach
D = {}


def king_path_rec(A, r, k):
    n = len(A)
    if (r, k) in D:
        return D[(r, k)]

    if r == 0 and k == 0:
        D[(r, k)] = 0
        return 0

    val = A[r][k]

    if r == 0:
        val += king_path_rec(A, r, k-1)

    elif k == 0:
        val += king_path_rec(A, r-1, k)

    else:
        val += min(king_path_rec(A, r-1, k), king_path_rec(A, r, k-1))

    D[(r, k)] = val
    return val
