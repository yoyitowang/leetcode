class BellManFord:
    def __init__(self, vertices):
        self.V = vertices
        self.dist = [float('inf')] * vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def find_shortest_path(self, source):
        self.dist[source] = 0
        
        for _ in range(self.V-1):
            updated = False
            for u, v, w in self.graph:
                if self.dist[u] + w < self.dist[v]:
                    self.dist[v] = self.dist[u] + w
                    updated = True

            if not updated:
                break

        for u, v, w in self.graph:
            if self.dist[u] + w < self.dist[v]:
                print("circle")
                exit()
        return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    mbf = BellManFord(n+1)

    for _ in range(m):
        u, v, w = map(int, input().split())
        mbf.add_edge(u, v, w)

    if mbf.find_shortest_path(1):
        ans = mbf.dist[n]
        if ans != float('inf'):
            print(ans)
        else: # can't arrive final vertex
            print("unconnected")

---
# SPFA
from collections import defaultdict, deque

class SPFA:
    def __init__(self, vertices):
        self.V = vertices
        self.dist = [float('inf')] * vertices
        self.graph = defaultdict(list)
        self.count = [0] * vertices

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def find_shortest_path(self, source):
        in_queue = [False] * self.V
        que = deque([source])
        # init
        self.dist[source] = 0
        in_queue[source] = True
        
        while que:
            u = que.popleft()
            in_queue[u] = False

            for v, w in self.graph[u]:
                if self.dist[u] + w < self.dist[v]:
                    self.dist[v] = self.dist[u] + w
                
                    if not in_queue[v]:
                        self.count[v] += 1
                        if self.count[v] >= self.V:
                            print("circle")
                            exit()
                        que.append(v)
                        in_queue[v] = True
        
if __name__ == '__main__':
    n, m = map(int, input().split())
    spfa = SPFA(n+1)

    for _ in range(m):
        u, v, w = map(int, input().split())
        spfa.add_edge(u, v, w)

    spfa.find_shortest_path(1)
    ans = spfa.dist[n]
    if ans != float('inf'):
        print(ans)
    else: # can't arrive final vertex
        print("unconnected")
        