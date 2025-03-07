# DFS
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or arr[i][j] != 1:
        return
    
    if arr[i][j] == 1:
        visited[i][j] = True
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

def main():
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)
            
main()

# BFS
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(i, j):
    from collections import deque
    que = deque([])
    que.append([i, j])
    visited[i][j] = True

    while que:
        x, y = que.popleft()
        for dx, dy in direction:
            x_next = x + dx
            y_next = y + dy
            if 0 <= x_next < n and 0 <= y_next < m and arr[x_next][y_next] == 1 and visited[x_next][y_next] == False:
                visited[x_next][y_next] = True
                que.append([x_next, y_next])

def main():
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == False:
                cnt += 1
                bfs(i, j)

    print(cnt)
            
main()