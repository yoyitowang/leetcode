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
from collections import deque, defaultdict

class SPFA:
    def __init__(self, vertices):
        self.V = vertices
        self.dist = [float('inf')] * vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def get_path(self, target):
        pass

    def find_shortest_costs(self, source, target):
        in_que = [False] * self.V
        self.dist[source] = 0
        in_que[source] = True
        que = deque([source])
        count = [0] * self.V

        while que:
            u = que.popleft()
            in_que[u] = False

            for v, w in self.graph[u]:
                if self.dist[u] + w < self.dist[v]:
                    self.dist[v] = self.dist[u] + w
                    
                    if not in_que[v]:
                        count[v] += 1
                        if count[v] >= self.V:
                            return 'circle'
                        que.append(v)
                        in_que[v] = True
                        
        return "unconnected" if self.dist[target] == float('inf') else self.dist[target]


if __name__ == "__main__":
    n, m = map(int, input().split())
    spfa = SPFA(n+1)

    for _ in range(m):
        u, v, w = map(int, input().split())
        spfa.add_edge(u, v, w)

    result = spfa.find_shortest_costs(1, n)
    print(result)