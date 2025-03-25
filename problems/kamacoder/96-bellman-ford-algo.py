from collections import deque, defaultdict

class BellManFord:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.dist = [float('inf')] * vertices

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_shortest_path(self, source, target, k):
        self.dist[source] = 0
        
        for _ in range(k+1):
            updated = False
            dist_copy = self.dist.copy()
            for u, v, w in self.graph:
                if dist_copy[u] != float('inf') and dist_copy[u] + w < self.dist[v]:
                    self.dist[v] = dist_copy[u] + w
                    updated = True
            if not updated:
                break
        
        if self.dist[target] == float('inf'):
            return 'unreachable'
        return self.dist[target]
                

if __name__ == '__main__':
    n, m = map(int, input().split())
    mbf = BellManFord(n+1)

    for _ in range(m):
        u, v, w = map(int, input().split())
        mbf.add_edge(u, v, w)
    source, target, k = map(int, input().split())


    res = mbf.find_shortest_path(source, target, k)
    print(res)