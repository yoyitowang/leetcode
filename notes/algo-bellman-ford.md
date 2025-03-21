# 1. Bellman-Ford 算法核心原理

## 1.1 基本思想
Bellman-Ford 算法基於**動態規劃**的思想，其核心是通過反覆的鬆弛操作來找到最短路徑。

### 動態規劃遞推公式
對於從源點 s 到節點 v 的最短路徑：
\[d[v] = \min_{(u,v) \in E}\{d[u] + w(u,v)\}\]

其中：
- d[v] 是從源點到節點 v 的最短距離
- w(u,v) 是邊 (u,v) 的權重

## 1.2 算法步驟詳解

```python
def bellman_ford(graph, source, V):
    # 1. 初始化
    dist = [float('inf')] * V
    dist[source] = 0
    parent = [-1] * V
    
    # 2. 鬆弛操作
    for i in range(V-1):
        for u, v, w in graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                
    # 3. 檢測負權環
    for u, v, w in graph:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None  # 存在負權環
            
    return dist, parent
```

### 為什麼需要 V-1 次迭代？
考慮最壞情況：
```
A → B → C → D → E
1   1   1   1
```
如果源點是 A，最壞情況下需要 4 次迭代（V-1=4）才能更新到 E 的正確距離。

# 2. 為什麼 Dijkstra 不能處理負權邊？

## 2.1 Dijkstra 的貪心策略失效
讓我們看一個具體例子：
```
A → B → C
2  -3   1
```

Dijkstra 算法執行過程：
1. 選擇 A 作為起點，dist[A]=0
2. 更新 B：dist[B]=2
3. **標記 B 為已訪問**（這是關鍵問題）
4. 更新 C：dist[C]=3
5. 但實際上 A→B→C 的距離是 0

問題在於：Dijkstra 算法一旦標記節點為已訪問，就永遠不會再更新該節點，這在有負權邊時會導致錯誤結果。

# 3. 最短路徑算法比較

| 算法 | 時間複雜度 | 空間複雜度 | 負權邊 | 負權環 | 適用場景 |
|------|------------|------------|--------|--------|----------|
| Dijkstra | O((V+E)logV) | O(V) | ❌ | ❌ | 非負權圖 |
| Bellman-Ford | O(VE) | O(V) | ✅ | 可檢測 | 含負權圖 |
| Floyd-Warshall | O(V³) | O(V²) | ✅ | 可檢測 | 多源最短路 |
| SPFA | 平均O(E) | O(V) | ✅ | 可檢測 | 含負權圖 |

## 3.1 具體比較

### Dijkstra vs Bellman-Ford
```python
# Dijkstra的核心（貪心）
while pq:
    dist_u, u = heapq.heappop(pq)
    if visited[u]:
        continue
    visited[u] = True  # 一旦訪問就不再更新

# Bellman-Ford的核心（動態規劃）
for i in range(V-1):
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w  # 可以多次更新
```

### SPFA (Shortest Path Faster Algorithm)
SPFA 是 Bellman-Ford 的隊列優化版本：
```python
def spfa(graph, source, V):
    dist = [float('inf')] * V
    dist[source] = 0
    in_queue = [False] * V
    queue = deque([source])
    
    while queue:
        u = queue.popleft()
        in_queue[u] = False
        
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
```

# 4. 實際應用場景分析

## 4.1 貨幣匯率套利系統
```python
def find_arbitrage(rates):
    """
    rates[i][j] 表示貨幣i兌換到貨幣j的匯率
    """
    V = len(rates)
    # 轉換為負對數權重
    graph = []
    for i in range(V):
        for j in range(V):
            if i != j:
                weight = -math.log(rates[i][j])
                graph.append((i, j, weight))
                
    # 運行Bellman-Ford
    dist = bellman_ford(graph, 0, V)
    if dist is None:
        print("存在套利機會！")
```

## 4.2 網絡時延分析
```python
def analyze_network_delay(topology):
    """
    分析網絡中可能的時延問題
    """
    class NetworkPacket:
        def __init__(self, delay, jitter):
            self.delay = delay
            self.jitter = jitter  # 可能為負值
            
    def convert_to_graph(topology):
        graph = []
        for node in topology:
            for neighbor, packet in node.connections.items():
                # 考慮時延和抖動
                graph.append((node.id, neighbor, 
                            packet.delay + packet.jitter))
        return graph
```

# 5. 優化技巧

## 5.1 提前終止優化
```python
def bellman_ford_optimized(graph, source, V):
    dist = [float('inf')] * V
    dist[source] = 0
    
    for i in range(V-1):
        updated = False
        for u, v, w in graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        # 如果這輪沒有更新，提前結束
        if not updated:
            break
```

## 5.2 隊列優化（SPFA）
```python
def spfa_with_negative_cycle_detection(graph, source, V):
    dist = [float('inf')] * V
    dist[source] = 0
    in_queue = [False] * V
    queue = deque([source])
    count = [0] * V  # 記錄入隊次數
    
    while queue:
        u = queue.popleft()
        in_queue[u] = False
        
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                count[v] += 1
                
                # 檢測負權環
                if count[v] >= V:
                    return None
                    
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
```

# 6. 實戰示例：路徑重建和可視化

```python
class BellmanFordVisualizer:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.iterations = []
        
    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))
        
    def visualize_iteration(self, dist, iteration):
        """記錄每次迭代的狀態"""
        self.iterations.append({
            'iteration': iteration,
            'distances': dist.copy()
        })
        
    def run_with_visualization(self, source):
        dist = [float('inf')] * self.V
        dist[source] = 0
        parent = [-1] * self.V
        
        # 記錄初始狀態
        self.visualize_iteration(dist, 0)
        
        # 主循環
        for i in range(self.V - 1):
            updated = False
            for u, v, w in self.graph:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    updated = True
            
            # 記錄這次迭代的狀態
            self.visualize_iteration(dist, i + 1)
            
            if not updated:
                break
                
        # 檢測負權環
        for u, v, w in self.graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return None, None
                
        return dist, parent
        
    def plot_progress(self):
        """繪製算法執行過程的可視化圖表"""
        import matplotlib.pyplot as plt
        
        iterations = [i['iteration'] for i in self.iterations]
        distances = np.array([i['distances'] for i in self.iterations])
        
        plt.figure(figsize=(12, 6))
        for v in range(self.V):
            plt.plot(iterations, distances[:, v], 
                    marker='o', label=f'Node {v}')
            
        plt.title('Bellman-Ford Algorithm Progress')
        plt.xlabel('Iteration')
        plt.ylabel('Distance from Source')
        plt.legend()
        plt.grid(True)
        plt.show()
```

# 7. 進階應用：處理不確定性

## 7.1 概率邊權重
```python
def probabilistic_bellman_ford(graph, source, V, samples=1000):
    """處理邊權重為概率分佈的情況"""
    results = []
    
    for _ in range(samples):
        # 生成這次模擬的確定性圖
        current_graph = []
        for u, v, dist_params in graph:
            # 從分佈中採樣權重
            w = np.random.normal(dist_params['mean'], 
                               dist_params['std'])
            current_graph.append((u, v, w))
            
        # 運行Bellman-Ford
        dist, _ = bellman_ford(current_graph, source, V)
        if dist:
            results.append(dist)
            
    # 統計分析
    return {
        'mean': np.mean(results, axis=0),
        'std': np.std(results, axis=0),
        'confidence_interval': np.percentile(results, 
                                          [2.5, 97.5], axis=0)
    }
```

# 8. 性能優化建議

1. **使用鄰接表**：對於稀疏圖更高效
```python
graph = defaultdict(list)
for u, v, w in edges:
    graph[u].append((v, w))
```

2. **並行化處理**：對於大規模圖
```python
def parallel_bellman_ford(graph, source, V, num_threads=4):
    from concurrent.futures import ThreadPoolExecutor
    
    def process_edges(edge_subset):
        updated = False
        for u, v, w in edge_subset:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        return updated
        
    # 將邊分成多個子集
    edge_subsets = np.array_split(graph, num_threads)
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for _ in range(V-1):
            results = list(executor.map(process_edges, edge_subsets))
            if not any(results):
                break
```

3. **記憶化優化**：對於重複計算
```python
@lru_cache(maxsize=None)
def get_shortest_path(source, target):
    """緩存常用的路徑計算結果"""
    pass
```
