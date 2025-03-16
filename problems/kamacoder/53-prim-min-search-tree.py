import heapq
from collections import defaultdict

class PrimMST:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        # graph {u: [(v, weight)]}
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self):
        # init a start vertex
        start_vertex = 0
        # check vertex is visited
        visited = [False] * self.V
        min_weight = [10001] * self.V
        edge_count = 0
        
        # priority queue: (weight, vertex)
        pq = [(0, start_vertex)] 
        while pq and edge_count < self.V:
            weight, current = heapq.heappop(pq)
            
            # if vertex is visited, skip 
            if visited[current]:
                continue
            
            visited[current] = True # marked as visited
            edge_count += 1         # edge count plus 1
            min_weight[current] = min(min_weight[current], weight) # update the min weight of i-th vertex

            # check the neighborhood of vertex and append the vertex into priority queue
            for next_vertex, next_weight in self.graph[current]:
                if not visited[next_vertex]:
                    heapq.heappush(pq, (next_weight, next_vertex))
        
        return min_weight

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
        self.uf = UnionFind(vertex)

    def add_edge(self, u, v, weight):
        heapq.heappush(self.pq, (weight, (u, v)))

    def kruskal_mst(self):
        
        min_weight = 0
        edge_count = 0
        n = len(self.pq)
        
        for _ in range(n):
            weight, (v1, v2) = heapq.heappop(self.pq)
            if not self.uf.union(v1, v2):
                min_weight += weight
                edge_count += 1
            
            if edge_count == self.V:
                break
        return min_weight
        
        

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