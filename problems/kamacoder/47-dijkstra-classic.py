class DijkstraClassic:
    def __init__(self, vertices):
        self.V = vertices
        # 初始化鄰接矩陣，使用float('inf')表示不連通
        self.graph = [[float('inf')] * vertices for _ in range(vertices)]
        # 對角線（自己到自己）設為0
        for i in range(vertices):
            self.graph[i][i] = 0
        
    def min_distance(self, dist, visited):
        """ find the unvisited and closet vertex"""
        min_distance = float('inf')
        min_vertex = -1

        for v in range(self.V):
            if not visited[v] and dist[v] < min_distance:
                min_distance = dist[v]
                min_vertex = v

        return min_vertex
        
    def dijkstra(self, source):
        # init dist array and visited mark
        dist = [float('inf')] * self.V
        dist[source] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            # find the closert vertex
            u = self.min_distance(dist, visited)
            if u == -1:
                continue

            visited[u] = True
            # update u to attached vertex dist
            for v in range(self.V):
                if not visited[v] and self.graph[u][v] != float('inf'):
                    dist[v] = min(dist[v], dist[u] + self.graph[u][v])
                    
        return dist

def solve():
    # 讀取輸入
    N, M = map(int, input().split())
    
    # 創建Dijkstra實例，注意頂點編號從1開始，所以大小為N+1
    dijkstra = DijkstraClassic(N + 1)
    
    # 讀取邊並構建圖
    for _ in range(M):
        s, e, v = map(int, input().split())
        dijkstra.graph[s][e] = v
    
    # 計算從起點(1)到所有點的最短距離
    distances = dijkstra.dijkstra(1)
    
    # 返回到終點(N)的距離，如果是無窮大表示不可達
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
        self.graph = [[float('inf')] * vertices for _ in range(vertices)]
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