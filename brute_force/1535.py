N = int(input())
hp = list(map(int,input().split()))
happy = list(map(int,input().split()))

dp = [[0]*101 for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(100):
        if j < hp[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-hp[i-1]]+happy[i-1])
print(dp[N][99])
    
