n, m = map(int, input().split())

edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))

from collections import defaultdict
ht = defaultdict(list)
for start, end in edges:
    ht[start].append(end)

ans = []
path = []
def dfs(graph, i, n):
    if i == n:
        ans.append(path.copy())
        return

    for _next in graph[i]:
        path.append(_next)
        dfs(graph, _next, n)
        path.pop()

def main():
    path.append(1)
    dfs(ht, 1, n)
    if not ans:
        print(-1)
    for p in ans:
        print(' '.join(map(str, p)))
main()