from collections import deque


def bfs(start):
    queu = deque([start])
    cnt = -1
    check[start] = True
    while queu:
        start = queu.popleft()
        cnt += 1
        for i in graph[start]:
            if not check[i]:
                if not graph[i]:
                    cnt -= 1
                check[i] = True
                queu.append(i)
                if i == 10:
                    ans.append(cnt)
    
n = int(input())
arr = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
check = [False] *(n+1)
for i in range(n-1):
    for j in range(arr[i]):
        if i+j+2 > n:
            continue
        graph[i+1].append(i+j+2)
ans = []
bfs(1)
if not ans:
    print(-1)
else:
    print(min(ans))
