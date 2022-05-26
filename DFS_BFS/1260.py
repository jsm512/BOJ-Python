from collections import deque
def dfs(graph,v,check):
    check[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not check[i]:
            dfs(graph,i,check)

def bfs(graph,v,check):
    queu = deque([v])
    check[v] = True
    while queu:
        v = queu.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not check[i]:
                queu.append(i)
                check[i] = True

n,m,v = map(int,input().split())
check_1=[False]*(n+1)
check_2=[False]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    prev,nxt=map(int,input().split())
    graph[prev].append(nxt)
    graph[nxt].append(prev)
for i in graph:
    i.sort()

dfs(graph,v,check_1)
print()
bfs(graph,v,check_2)