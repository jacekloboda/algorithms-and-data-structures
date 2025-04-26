# tresc
# Układ planetarny Algon składa się z n planet o numerach od 0 do n − 1. Niestety własności fizyczne
# układu powodują, że nie da się łatwo przelecieć między dowolnymi dwiema planetami. Na szczęście
# mozolna eksploracja kosmosu doprowadziła do stworzenia listy E dopuszczalnych bezpośrednich
# przelotów. Każdy element listy E to trójka postaci (u, v, t), gdzie u i v to numery planet (można
# założyć, że u < v) a t to czas podróży między nimi (przelot z u do v trwa tyle samo co z v do u).
# Dodatkową nietypową własnością układu Algon jest to, że niektóre planety znajdują się w okolicy
# osobliwości. Znajdując się przy takiej planecie możliwe jest zagięcie czasoprzestrzeni umożliwiające
# przedostanie się do dowolnej innej planety leżącej przy osobliwości w czasie zerowym.
# Zadanie polega na zaimplementowaniu funkcji:
# def spacetravel( n, E, S, a, b )
# która zwraca najkrótszy czas podróży z planety a do planety b, mając do dyspozycji listę możliwych
# bezpośrednich przelotów E oraz listę S planet znajdujących się koło osobliwości. Jeśli trasa nie
# istnieje, to funkcja powinna zwrócić None.

# rozwizanie
# tworze liste sasiedztwa z wagami, kazdy wierzcholke przy odobliwosci dostaje krawedz wagi 0 do urojonego wierzcholka osobliwosci
# algorytmem dijkstry szukam najkrotszej sciezki z a do b i ja zwracam
# zlozonosc czasowa: O(ElogV)

def spacetravel(n, E, S, a, b):

    def dijkstra(G, s):  # dijkstra algorithm

        import heapq

        n = len(G)
        D = [float('inf') for _ in range(n)]
        D[s] = 0
        Q = [(0, s)]

        while Q:

            # print(Q)
            dist, u = heapq.heappop(Q)

            if dist > D[u]:
                continue

            # print(u, dist)

            for w, v in G[u]:

                if D[u] + w < D[v]:
                    # print(v, D[v], D[u] + w)

                    D[v] = D[u] + w
                    heapq.heappush(Q, (D[v], v))

        return D

    G = [[] for _ in range(n+1)]

    for start, end, weight in E:

        G[start].append((weight, end))
        G[end].append((weight, start))

    for node in S:

        G[node].append((0, n))
        G[n].append((0, node))

    D = dijkstra(G, a)

    if D[b] == float('inf'):
        return None

    return D[b]
