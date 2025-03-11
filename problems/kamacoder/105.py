n, k = map(int, input().split())

from collections import defaultdict, deque

ht = defaultdict(list)
for _ in range(k):
    start, end = map(int, input().split())
    ht[start].append(end)
visit = [False for _ in range(n+1)]

def dfs(i):
    visit[i] = True
    num = 1

    for _next in ht[i]:
        if not visit[_next]:
            num += dfs(_next)

    return num

def bfs(i):
    visit[i] = True
    num = 1
    que = deque([i])

    while que:
        _next = que.popleft()
        for _next in ht[_next]:
            if visit[_next] == False:
                num += 1
                visit[_next] = True
                que.append(_next)

    return num

def main():

    # ans = dfs(1)
    ans = bfs(1)
    print(1 if ans == n else -1)

main()
    
    