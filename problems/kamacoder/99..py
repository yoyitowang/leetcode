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