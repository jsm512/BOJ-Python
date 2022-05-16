n,k=map(int,input().split())

input_coin=[]
for i in range(n):
    input_coin.append(int(input()))
input_coin.sort(reverse=True)

ans = 0
for i in range(n):
    if (k // input_coin[i] != 0):
        ans += k // input_coin[i]
        k %= input_coin[i]

print(ans)


