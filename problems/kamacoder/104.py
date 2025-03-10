# DFS
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

from collections import defaultdict
areaMap = defaultdict(int)

def dfs(i: int, j: int, num):
    visited[i][j] = True
    arr[i][j] = num
    area = 1

    for dx, dy in directions:
        x, y = i+dx, j+dy
        if 0 <= x < n and 0 <= y < m and arr[x][y] == 1 and visited[x][y] == False:
            area += dfs(x, y, num)
    
    return area

def main():

    num = 1
    max_area = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 1:
                num += 1
                areaMap[num] = dfs(i, j, num)
                max_area = max(max_area, areaMap[num])

    if max_area == n*m:
        print(max_area)
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                tmp = 1
                neighbor = set()
                for dx, dy in directions:
                    x, y = i+dx, j+dy
                    if 0 <= x < n and 0 <= y < m:
                        neighbor.add(arr[x][y])
                for num in neighbor:
                    tmp += areaMap[num]
                max_area = max(max_area, tmp)
    print(max_area)

main()