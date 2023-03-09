from collections import deque


def bfs(graph,v,check):
    queu = deque([v])
    check[v] = True
    while queu:
        v = queu.popleft()
        for i in graph[v]:
            if not check[i]:
                queu.append(i)
                check[i] = True
                ans[i] = v

n = int(input())
graph = [[] for _ in range(n+1)]
ans = [0 for _ in range(n+1)]
check = [False]*(n+1)
for _ in range(n-1):
    prev,nxt = map(int,input().split())
    graph[prev].append(nxt)
    graph[nxt].append(prev)
for i in graph:
    i.sort()
bfs(graph,1,check)
for i in range(2,len(ans)):
    print(ans[i])