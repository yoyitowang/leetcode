# DFS
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def dfs(i: int, j: int):
    # start from a point and dfs to all touched land
    # return isolated(bool), area(int)
    isolated = True
    visited[i][j] = True
    area = 1

    for dx, dy in directions:
        x, y = i + dx, j + dy
        if x < 0 or y < 0 or n <= x or m <= y:
            isolated = False
        elif arr[x][y] == 1 and visited[x][y] == False:
            visited[x][y] = True
            _isolated, _area = dfs(x, y)
            isolated &= _isolated
            area += _area
            
    return isolated, area

def main():
    # check and calculate each value
    ans = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visited[i][j]:
                isolated, area = dfs(i, j)
                if isolated:
                    ans += area
    print(ans)

main()