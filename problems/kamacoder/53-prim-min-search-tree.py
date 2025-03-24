from collections import defaultdict
import heapq

class PrimMST:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def find_shortest_path(self, source):
        # init a vertex and add to min tree
        # find the cloest vertex of the tree by minmum weight
        # update the minmum queue and tree

        # init each vertex distance in minmum tree => inf, start vertex is 0
        min_dist = [float('inf')] * self.V
        min_dist[source] = 0
        edge_count = 0
        # when vertex is visited, no need to add into minmum tree
        visited = [False] * self.V 
        # priority queue is used to update and add the new vertex to tree
        pq = [(0, source)]

        while pq and edge_count < self.V:
            weight, u = heapq.heappop(pq)

            if visited[u]: # already in tree
                continue

            visited[u] = True
            min_dist[u] = min(min_dist[u], weight) # update the minmum weight of vertex in tree
            edge_count += 1

            # add the cloest vertex into queue
            for v, w in self.graph[u]:
                if not visited[v]: # add unvisited vertex into queue and waiting for updating
                    heapq.heappush(pq, (w, v))
        return min_dist

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * (size)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rX = self.find(x)
        rY = self.find(y)

        if rX != rY:
            if self.rank[rX] > self.rank[rY]:
                self.parent[rY] = rX
            elif self.rank[rX] < self.rank[rY]:
                self.parent[rX] = rY
            else:
                self.parent[rY] = rX
                self.rank[rX] += 1
            return False

        return True

    def isSame(self, x, y):
        return self.find(x) == self.find(y)

class Kruskal:
    def __init__(self, vertex):
        self.V = vertex
        self.pq = []
    
    def add_edge(self, u, v, w):
        heapq.heappush(self.pq, (w, (u, v)))

    def find_shortest_path(self, source):
        uf = UnionFind(self.V)
        min_dist = 0
        count = 0
        
        while self.pq and count < self.V:
            w, (u, v) = heapq.heappop(self.pq)
            
            if uf.union(u, v):
                count += 1
                min_dist += w

        return min_dist

if __name__ == '__main__':
    # V, E = map(int, input().split())
    # prim = PrimMST(V)

    # for _ in range(E):
    #     v1, v2, val = map(int, input().split())
    #     prim.add_edge(v1-1, v2-1, val)
    # # prim.print_mst()
    # weight = prim.prim_mst()
    # print(sum(weight[1:]))
    # # mst_weight, _ = prim.prim_mst()
    # # print(mst_weight)


    V, E = map(int, input().split())
    krus = Kruskal(V)

    for _ in range(E):
        v1, v2, val = map(int, input().split())
        krus.add_edge(v1-1, v2-1, val)

    # print(krus.pq)
    ans = krus.kruskal_mst()
    print(ans)