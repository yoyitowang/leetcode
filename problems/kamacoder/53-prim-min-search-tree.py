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
import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx != ry:
            if self.rank[rx] > self.rank[ry]:
                self.parent[ry] = rx
            elif self.rank[rx] < self.rank[ry]:
                self.parent[rx] = ry
            else:
                self.parent[ry] = rx
                self.rank[rx] += 1
            return True
        return False

class Kruskal:
    def __init__(self, vertex):
        self.V = vertex
        self.pq = []

    def add_edge(self, u, v, w):
        # push all edge into priority queue
        heapq.heappush(self.pq, (w, (u, v)))

    def find_shortest_path(self, source):
        # get the shortest weight of edge and check are u and v in the same group(use the union find)
        uf = UnionFind(self.V)
        visited = [False] * self.V
        min_dist = 0
        edge_count = 0
        
        while self.pq and edge_count < self.V:
            w, (u, v) = heapq.heappop(self.pq)
            # can union -> not same group
            if uf.union(u, v):
                min_dist += w
                edge_count += 1
                
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