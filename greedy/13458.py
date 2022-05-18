import sys


n = int(input())
arr = list(map(int,sys.stdin.readline().split()))
b,c = map(int,sys.stdin.readline().split())

ans = 0

for i in range(n):
    if arr[i] > 0:
        arr[i] -= b
        ans+=1
    if arr[i] > 0:
        ans += int(arr[i]/c)
        if arr[i] % c != 0:
            ans += 1
print(ans)

