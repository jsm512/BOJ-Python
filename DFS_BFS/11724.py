import sys
sys.setrecursionlimit(10**6)

def dfs(start):
    check[start] = True
    for i in arr[start]:
        if not check[i]:
            dfs(i)
n,m = map(int,sys.stdin.readline().split())
check = [False]*(n+1)
cnt = 0
arr = [[] for i in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()


for i in range(1,n+1):
    if check[i] == False:
        if not arr[i]:
            cnt+=1
            check[i] = True
        else:
            dfs(i)
            cnt+=1
print(cnt)