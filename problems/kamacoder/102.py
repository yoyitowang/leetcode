# DFS
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def dfs(i, j):
    if arr[i][j] != 1:
        return 

    arr[i][j] = 2
    
    for dx, dy in directions:
        x, y = i+dx, j+dy
        if 0 <= x < n and 0 <= y < m and arr[x][y] == 1:
            dfs(x, y)

def main():
    # first/last column
    for i in range(n): # O(n)
        dfs(i, 0)
        dfs(i, m-1)

    # first/last row
    for j in range(m): # O(m)
        dfs(0, j)
        dfs(n-1, j)

    for i in range(n): # O(n*m)
        for j in range(m):
            if arr[i][j] == 1: arr[i][j] = 0

    for i in range(n): # O(n*m)
        for j in range(m):
            if arr[i][j] == 2: arr[i][j] = 1

    for row in arr: # O(n*m)
        print(' '.join(map(str, row)))

# TC: O(n*m)
# SC: O(n*m)
main()
