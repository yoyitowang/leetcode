from collections import deque, defaultdict

class bellman_ford:
    def __init__(self, vertices):
        self.V = vertices
        self.dist = [float('inf')] * vertices
        self.graph = []
        self.parent = [-1] * vertices
        self.count = 0

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def get_path(self, target):
        path = []
        cur = target
        while cur != -1:
            path.append(cur)
            cur = self.parent[cur]
            
        return path[::-1]

    def find_shortest_costs(self, source):
        visited = [False] * self.V
        self.dist[source] = 0

        for _ in range(self.V-1):
            updated = False
            for u, v, w in self.graph:
                if self.dist[u] != float('inf') and self.dist[u] + w < self.dist[v]:
                    self.dist[v] = self.dist[u] + w
                    self.parent[v] = u
                    updated = True
            if not updated:
                break

        for u, v, w in self.graph:
                if self.dist[u] != float('inf') and self.dist[u] + w < self.dist[v]:
                    return False

        return True

if __name__ == "__main__":
    n, m = map(int, input().split())
    bellman = bellman_ford(n+1)

    for _ in range(m):
        u, v, w = map(int, input().split())
        bellman.add_edge(u, v, w)

    if bellman.find_shortest_costs(1) and bellman.dist[n] != float('inf'):
        print(bellman.dist[n])
        print(bellman.get_path(n))
    else:
        print("unconnected")

---
# SPFA
from collections import deque, defaultdict

class SPFA:
    def __init__(self, vertices):
        self.V = vertices
        self.dist = [float('inf')] * vertices
        self.graph = defaultdict(list)
        self.parent = [-1] * vertices
        self.count = [0] * vertices

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def get_path(self, target):
        path = []
        cur = target
        while cur != -1:
            path.append(cur)
            cur = self.parent[cur]
            
        return path[::-1]

    def find_shortest_costs(self, source):
        que = deque([source])
        in_que = [False] * self.V
        self.dist[source] = 0

        while que:
            u = que.popleft()
            in_que[u] = False
            
            for v, w in self.graph[u]:
                if self.dist[u] + w < self.dist[v]:
                    self.dist[v] = self.dist[u] + w
                    self.parent[v] = u
                
                    if not in_que[v]:
                        self.count[v] += 1
                        if self.count[v] >= self.V:
                            return False
                        que.append(v)
                        in_que[v] = True
        return True

if __name__ == "__main__":
    n, m = map(int, input().split())
    spfa = SPFA(n+1)

    for _ in range(m):
        u, v, w = map(int, input().split())
        spfa.add_edge(u, v, w)

    if spfa.find_shortest_costs(1):
        if spfa.dist[n] != float('inf'):
            print(spfa.dist[n])
            print(spfa.get_path(n))
            exit()
    print("unconnected")
