from collections import deque, defaultdict

class bellman_ford:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.min_dist = [float('inf')] * self.V
        self.parent = [-1] * vertices

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def get_path(self, target):
        res = []
        cur = target
        while cur != -1:
            res.append(cur)
            cur = self.parent[cur]
        if res[-1] != 1:
            return []
        return res[::-1]

    def find_shortest_costs(self, source):
        self.min_dist[source] = 0

        for _ in range(self.V-1):
            updated = False
            for u, v, w in self.graph:
                if self.min_dist[u] != float('inf') and self.min_dist[u] + w < self.min_dist[v]:
                    self.min_dist[v] = self.min_dist[u] + w
                    self.parent[v] = u
                    updated = True
        
            if not updated:
                break
        
        for u, v, w in self.graph:
            if self.min_dist[u] != float('inf') and self.min_dist[u] + w < self.min_dist[v]:
                return False

        return True

if __name__ == "__main__":
    n, m = map(int, input().split())
    bellman = bellman_ford(n+1)

    for _ in range(m):
        u, v, w = map(int, input().split())
        bellman.add_edge(u, v, w)

    if bellman.find_shortest_costs(1) and bellman.min_dist[n] != float('inf'):
        print(bellman.min_dist[n])
        print(bellman.get_path(n))
    else:
        print("unconnected")

---
# SPFA
from collections import deque, defaultdict

class SPFA:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.dist = [float('inf')] * vertices
        self.parent = [-1] * vertices

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def get_path(self, target):
        ans = []
        cur = target
        while cur != -1:
            ans.append(cur)
            cur = self.parent[cur]

        if ans[-1] != 1:
            return []
        return ans[::-1]

    def find_shortest_costs(self, source):
        self.dist[source] = 0
        count = [0] * self.V
        visited = [False] * self.V
        que = deque([source])

        while que:
            u = que.popleft()
            visited[u] = False
            
            for v, w in self.graph[u]:
                if self.dist[u] + w < self.dist[v]:
                    self.dist[v] = self.dist[u] + w
                    self.parent[v] = u

                    if not visited[v]:
                        count[v] += 1
                        if count[v] >= self.V:
                            return False
                        if que and self.dist[v] < self.dist[que[0]]:
                            que.appendleft(v)
                        else:
                            que.append(v)
                        visited[v] = True
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
            # print(spfa.get_path(n))
            exit()
    print("unconnected")