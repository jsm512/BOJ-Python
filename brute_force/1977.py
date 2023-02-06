m = int(input())
n = int(input())

min_value = 0
ans = 0

for i in range(1,101):
    if m <= i*i <= n:
        if ans == 0:
            min_value = i*i
        ans += i*i

if ans != 0:
    print(ans)
    print(min_value)
else:
    print(-1)