n = int(input())

beginStr, endStr = input().split()
strList = [input().strip() for _ in range(n)]

def check(str1, str2):
    cnt = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            cnt += 1
    return cnt == 1

def main():
    if beginStr == endStr:
        print(0)
        return

    visit = [False for i in range(n)]
    from collections import deque
    que = deque([])
    que.append([beginStr, 1])

    while que:
        s, step = que.popleft()
        if check(s, endStr):
            print(step+1)
            exit()
        for i in range(n):
            ss = strList[i]
            if visit[i] == False and check(s, ss):
                visit[i] = True
                que.append([ss, step+1])
    print(0)
main()