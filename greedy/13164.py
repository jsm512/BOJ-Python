n,k = map(int,input().split())
length = list(map(int,input().split()))
ans = []
for i in range(n-1):
    ans.append(length[i+1] - length[i])
ans.sort()

sum = 0
for i in range(n-k):
    sum += ans[i]
print(sum)