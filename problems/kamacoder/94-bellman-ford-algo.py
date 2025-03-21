class BellmanFord:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.dist = [float('inf')] * vertices
        
    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def find_shortest_costs(self, source):
        self.dist[source] = 0
        
        for i in range(self.V-1):
            updated = False
            for u, v, w in self.graph:
                if self.dist[u] != float('inf') and self.dist[u] + w < self.dist[v]:
                    self.dist[v] = self.dist[u] + w
                    updated = True
            
            if not updated:
                break

        for u, v, w in self.graph:
            if self.dist[u] != float('inf') and self.dist[u] + w < self.dist[v]:
                return False  # 存在負環

        return True
        

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    edges = []
    bell = BellmanFord(n+1)

    for _ in range(m):
        src, dest, weight = map(int, input().strip().split())
        bell.add_edge(src, dest, weight)

    if not bell.find_shortest_costs(1) or bell.dist[n] == float('inf'):
        print("unconnected")
    else:
        print(bell.dist[n])

