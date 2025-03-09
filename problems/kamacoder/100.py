# DFS
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def dfs(i, j, res=0):
    if i < 0 or j < 0 or i >= n or j >= m or arr[i][j] == 0 or visited[i][j] == True:
        return res
    res += 1
    visited[i][j] = True
    for dx, dy in directions:
        x_next = i + dx
        y_next = j + dy
        res = dfs(x_next, y_next, res)

    return res
    

def main():
    ans = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == False:
                ans = max(ans, dfs(i, j))

    print(ans)

main()

# BFS
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
from collections import deque
def bfs(i, j):
    que = deque([])
    que.append([i, j])
    visited[i][j] = True
    res = 1

    while que:
        x, y = que.popleft()
        for dx, dy in directions:
            x_next = x + dx
            y_next = y + dy
            if 0 <= x_next < n and 0 <= y_next < m and arr[x_next][y_next] == 1 and visited[x_next][y_next] == False:
                res += 1
                visited[x_next][y_next] = True
                que.append([x_next,  y_next])
            
    return res

def main():
    ans = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == False:
                ans = max(ans, bfs(i, j))

    print(ans)

main()


# BFS
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

from collections import deque

def bfs(i: int, j: int):
    # start from a point and dfs to all touched land
    # return isolated(bool), area(int)
    isolated = True
    visited[i][j] = True
    area = 1
    que = deque([])
    que.append([i, j])

    while que:
        ii, jj = que.popleft()

        for dx, dy in directions:
            x, y = ii+dx, jj+dy
            if x < 0 or y < 0 or n <= x or m <= y:
                isolated = False
            elif arr[x][y] == 1 and visited[x][y] == False:
                area += 1
                visited[x][y] = True
                que.append([x, y])

    return area if isolated else 0
            
    
def main():
    
    total = 0
    for row in arr:
        total += sum(row)
    if total >= n*m - 4 or n <= 2 or m <= 2:
        print(0)
        return

    # check and calculate each value
    ans = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visited[i][j]:
                ans += bfs(i, j)
    print(ans)

main()