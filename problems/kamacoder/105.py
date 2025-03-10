# DFS
n, k = map(int, input().split())

from collections import defaultdict
ht = defaultdict(list)
for _ in range(k):
    start, end = map(int, input().split())
    ht[start].append(end)
visit = [False for _ in range(n+1)]

def dfs(i):
    visit[i] = True
    cnt = 1
    for _next in ht[i]:
        if not visit[_next]:
            cnt += dfs(_next)

    return cnt

def main():
    cnt = dfs(1)
    print(1 if cnt==n else -1)

main()