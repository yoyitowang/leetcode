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
class DijkstraClassic:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(dict)
        for i in range(vertices):
            self.graph[i][i] = 0
        
    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        
    def dijkstra(self, source):
        import heapq
        # init dist array and visited mark
        dist = [float('inf')] * self.V
        dist[source] = 0 # start vertex
        visited = [False] * self.V
        pq = [(0, source)]

        # find the closest vertex
        while pq:
            weight, u = heapq.heappop(pq)
            visited[u] = True

            for v, w in self.graph[u].items():
                new_dist = dist[u] + w
                if not visited[v] and new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
            
        return dist