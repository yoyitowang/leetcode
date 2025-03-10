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

# BFS
n, k = map(int, input().split())

from collections import defaultdict, deque

ht = defaultdict(list)
for _ in range(k):
    start, end = map(int, input().split())
    ht[start].append(end)
visit = [False for _ in range(n+1)]

def bfs(i):
    cnt = 1
    que = deque([i])
    visit[i] = True
    
    while que:
        node = que.popleft()
        for _next in ht[node]:
            if visit[_next] == False:
                cnt += 1
                visit[_next] = True
                que.append(_next)

    return cnt

def main():
    if k == 0:
        print(1 if n == 1 else -1)
        return

    cnt = bfs(1)
    print(1 if cnt==n else -1)

main()