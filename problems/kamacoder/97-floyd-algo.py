def solve_park_routes():
    # 讀取景點數量和道路數量
    N, M = map(int, input().split())
    
    # 初始化距離矩陣
    dist = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    
    # 初始化對角線為0（自己到自己的距離為0）
    for i in range(1, N + 1):
        dist[i][i] = 0
    
    # 讀取道路信息並建立圖
    for _ in range(M):
        u, v, w = map(int, input().split())
        # 因為是雙向道路，所以兩個方向都要記錄
        dist[u][v] = w
        dist[v][u] = w
    
    # Floyd 算法核心部分
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # 讀取查詢數量
    Q = int(input())
    
    # 處理每個查詢
    for _ in range(Q):
        start, end = map(int, input().split())
        # 如果距離是無窮大，表示不存在路徑
        if dist[start][end] == float('inf'):
            print(-1)
        else:
            print(dist[start][end])

# 執行主函數
solve_park_routes()
