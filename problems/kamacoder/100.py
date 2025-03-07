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