class UnionFind:
    def __init__(self, n):
        self.N = n+1
        self.parent = [i for i in range(self.N)]
        self.rank = [1] * (self.N)
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx != ry:
            # assign smaller tree to bigger
            if self.rank[rx] > self.rank[ry]:
                self.parent[ry] = rx # set smaller root to the root of bigger tree
            elif self.rank[rx] < self.rank[ry]:
                self.parent[rx] = ry
            else:
                self.parent[rx] = ry
                self.rank[ry] += 1
            return True
        
        return False

    def findRedundantDirectedConnection(self, edges):
        parent = [i for i in range(self.N)]
        conflict_edges = None
        cycle_edges = None
        
        # find any in-degree = 2
        for u, v in edges:
            if parent[v] != v:
                conflict_edges = (u, v)
            else:
                parent[v] = u
                if not self.union(u, v):
                    cycle_edges = (u, v)

        if conflict_edges:
            if cycle_edges:
                return [parent[conflict_edges[1]], conflict_edges[1]]
            else:
                return conflict_edges
        return cycle_edges


def main():
    n = int(input())
    uf = UnionFind(n)
    edges = []
    for _ in range(n):
        u, v = map(int, input().split())
        edges.append([u, v])
    
    res = uf.findRedundantDirectedConnection(edges)
    print(res[0], res[1])
 

if __name__ == "__main__":
    main()
