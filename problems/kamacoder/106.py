n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# DFS
def dfs(i, j):
    visited[i][j] = True
    area = 0

    for dx, dy in directions:
        x, y = i+dx, j+dy
        if x < 0 or y < 0 or n <= x or m <= y or arr[x][y] == 0:
            area += 1
        if 0 <= x < n and 0 <= y < m and arr[x][y] == 1 and visited[x][y] == False:
            area += dfs(x, y)

    return area

# BFS
from collections import deque
def bfs(i, j):
    visited[i][j] = True
    area = 0
    que = deque()
    que.append([i, j])

    while que:
        ii, jj = que.popleft()
        for dx, dy in directions:
            x, y = ii+dx, jj+dy
            if x < 0 or y < 0 or n <= x or m <= y or arr[x][y] == 0:
                area += 1
            if 0 <= x < n and 0 <= y < m and arr[x][y] == 1 and visited[x][y] == False:
                visited[x][y] = True
                que.append([x, y])

    return area
    

def main():
    area = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 1:
                # area += dfs(i, j)
                area += bfs(i, j)
    print(area)
    

main()