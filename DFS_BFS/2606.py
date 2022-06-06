def dfs(start,cnt_arr):
    check[start] = True
    cnt_arr.append(start)
    for i in network[start]:
        if not check[i]:
            dfs(i,cnt_arr)
computer = int(input())
linked = int(input())
cnt_arr = []
network=[[] for _ in range(computer+1)]
check = [False]*(computer+1)
for _ in range(linked):
    f,n = map(int,input().split())
    network[f].append(n)
    network[n].append(f)

for i in network:
    i.sort()

dfs(1,cnt_arr)

print(len(cnt_arr)-1)

