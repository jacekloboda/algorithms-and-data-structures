# Dobrycerz (czyli rycerz, który zawsze uprzejmie mówi “dzień dobry”) chce się przedostać z zamku s
# do zamku t. Mapa zamków dana jest w postaci grafu nieskierowanego G, gdzie każda krawędź ma wa-
# gę oznaczającą ile godzin potrzeba, żeby ją przebyć. Wagi to liczby naturalne ze zbioru {1, 2, . . . , 8}.
# Po najdalej 16 godzinach podróży Dobrycerz musi nocować w zamku. Warunki uprzejmości wy-
# magają, żeby spędził w takim zamku 8 godzin (przejazd przez zamki, w których nie nocuje nie
# kosztuje dodatkowego czasu; szybko mówi “dzień dobry” strażnikom i jedzie dalej). Mapa z której
# korzysta Dobrycerz ma to do siebie, że liczba dróg jest proporcjonalna do liczby zamków. Czyli jeśli
# zamków jest n, to wiadomo, że dróg jest O(n).
# Zadanie polega na implementacji funkcji:
# goodknight( G, s, t )
# która na wejściu otrzymuje graf opisujący mapę zamków, reprezentowany w postaci macierzy są-
# siedztwa (czyli G[i][j] to liczba godzin, konieczna do przejechania bezpośrednio z zamku i do
# zamku j; w przypadku braku drogi G[i][j] = −1), zamek startowy s oraz zamek docelowy t, i
# zwraca minimalny czas (wyrażony w godzinach) potrzebny na przejazd z s do t (Dobrycerz nigdy
# nie musi nocować ani w zamku s ani w zamku t). Można założyć, że zawsze istnieje trasa z zamku
# s do t.
#
# rozwiazanie: przy uzyciu bfs i rozszerzania krawedzi, wagi krawedzi sa ograniczone przez stala wiec algorytm ma zlozonosc O(n^2)
# lista D ma osobne odleglosci w zaleznosci od czasu w jakim rycerz dotarl do wierzcholka, zeby nie poprawiac odleglosci na zlych sciezkach

def goodknight(G, s, t):

    from collections import deque

    n = len(G)
    D = [[float('inf')]*17 for _ in range(n)]
    D[s][0] = 0
    Q = deque([(s, 0, 0)])

    while Q:

        u, dist, time = Q.popleft()

        if 0 < dist:
            Q.append((u, dist-1, time))
            continue

        if D[u][time] < dist:
            continue

        if u == t:
            return D[u][time]

        for v in range(n):

            wgt = G[u][v]

            if wgt != -1:

                if 16 < time + wgt:  # rest

                    if D[u][time] + wgt + 8 < D[v][wgt]:

                        D[v][wgt] = D[u][time] + wgt + 8
                        Q.append((v, D[v][wgt], wgt))

                else:  # no rest

                    if D[u][time] + wgt < D[v][time+wgt]:

                        D[v][time+wgt] = D[u][time]+wgt
                        Q.append((v, D[v][time+wgt], time+wgt))
