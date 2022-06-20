def dfs(start,cnt):
    cnt+=1
    check[start] = True
    if start == p2:
        my_arr.append(cnt)
    for i in arr[start]:
        if not check[i]:
            dfs(i,cnt)

        
n = int(input())
p1,p2 = map(int,input().split())
m = int(input())
my_arr=[]
arr = [[] for i in range(n+1)]
check=[False]*(n+1)

for i in range(m):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

dfs(p1,0)

if len(my_arr) == 0:
    print(-1)
else:
    print(my_arr[0]-1)
