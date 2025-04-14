# DFS
n, m = map(int, input().split())

edges = []
for _ in range(n):
    edges.append(list(map(int, input().split())))

used = [[False] * m for _ in range(n)]
direction = [(1, 0), (0, 1), (0, -1), (-1, 0)]

def dfs(i, j):
    used[i][j] = True

    for dx, dy in direction:
        x = i + dx
        y = j + dy
        if 0 <= x < n and 0 <= y < m and edges[x][y] == 1 and not used[x][y]:
            dfs(x, y)

def main():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if edges[i][j] == 1 and not used[i][j]:
                dfs(i, j)
                cnt += 1
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