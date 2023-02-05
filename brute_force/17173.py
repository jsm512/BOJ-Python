n,m = map(int,input().split())
arr = list(map(int,input().split()))

ans = 0
for i in range(1,n+1):
    for j in arr:
        if i % j == 0:
            ans += i
            break
print(ans)
    