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
        
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
ans = [0 for _ in range(n+1)]
check = [False for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
bfs(1)
cnt = 0
for i in ans:
    if 0 < i <= 2:
        cnt += 1
print(cnt)