from collections import deque
import sys


def bfs(start):
    queu = deque([start])
    check[start] = True
    while queu:
        start = queu.popleft()
        for i in graph[start]:
            if not check[i]:
                queu.append(i)
                check[i] = True
                ans[i] = ans[start] + 1
        
n,m,k,x = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
ans = [0 for _ in range(n+1)]
check = [False for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
bfs(x)

if k not in ans:
    print(-1)
else:
    for i in range(len(ans)):
        if ans[i] == k:
            print(i)