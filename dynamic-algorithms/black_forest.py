# black forest
# T - list of value of i-th tree
# cant cut two trees next to each other
# find max sum of values

# recursive approach
def black_forest_rec(T):
    Df = {}
    Dg = {}

    def f(i):  # max sum form 0 to i with i-th tree cat down
        if i in Df:
            return Df[i]

        if i == 0:
            Df[i] = T[i]
            return T[i]

        Df[i] = T[i]+g(i-1)
        return Df[i]

    def g(i):  # max sum from 0 to i with i-th tree standing
        if i in Dg:
            return Dg[i]

        if i == 0:
            Dg[i] = 0
            return 0

        Dg[i] = max(g(i-1), f(i-1))
        return Dg[i]

    n = len(T)
    return max(f(n-1), g(n-1))


# iterative approach
def black_forest_it(T):
    n = len(T)
    f = g = 0
    for i in range(n):
        f, g = g + T[i], max(f, g)

    return max(f, g)
