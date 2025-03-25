from collections import defaultdict

class DijkstraClassic:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[float('inf')] * vertices for _ in range(vertices)]
        for i in range(vertices):
            self.graph[i][i] = 0
        
    def min_distance(self, dist, visited):
        min_distance = float('inf')
        min_vertex = -1

        for v in range(self.V):
            if not visited[v] and dist[v] < min_distance:
                min_distance = dist[v]
                min_vertex = v
        return min_vertex

    def dijkstra(self, source):
        dist = [float('inf')] * self.V
        dist[source] = 0
        visited = [False] * self.V
        
        for _ in range(self.V):
            u = self.min_distance(dist, visited)
            if u == -1:
                continue
            visited[u] = True

            for v in range(self.V):
                if not visited[v] and self.graph[u][v] != float('inf'):
                    dist[v] = min(dist[v], dist[u]+self.graph[u][v])

        return dist
                

def solve():
    N, M = map(int, input().split())
    
    dijkstra = DijkstraClassic(N + 1)
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        dijkstra.graph[u][v] = w
    
    # caculation starts from vertex = 1
    distances = dijkstra.dijkstra(1)

    # check last vertex, if it's inf -> not arriable    
    return distances[N] if distances[N] != float('inf') else -1

def main():
    result = solve()
    print(result)

if __name__ == "__main__":
    main()



---
from collections import defaultdict
import heapq

class DijkstraOptimized:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((w, v))
            
    def find_the_shortest_path(self, source):
        dist = [float('inf')] * self.V
        visited = [False] * self.V
        dist[source] = 0
        count = 0

        pq = [(0, source)]
        while pq and count < self.V:
            w, u = heapq.heappop(pq)

            visited[u] = True
            for weight, v in self.graph[u]:
                if not visited[v] and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[u]+weight, v))

        return dist

def solve():
    N, M = map(int, input().split())
    
    dijkstra = DijkstraOptimized(N + 1)
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        dijkstra.add_edge(u, v, w)
    
    # caculation starts from vertex = 1
    distances = dijkstra.find_the_shortest_path(1)

    # check last vertex, if it's inf -> not arriable    
    return distances[N] if distances[N] != float('inf') else -1

def main():
    result = solve()
    print(result)

if __name__ == "__main__":
    main()
