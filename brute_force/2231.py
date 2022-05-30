n = int(input())

ans = 0

for i in range(n):
    num = i
    my_sum = 0

    while num != 0:
        my_sum += num % 10
        num //= 10
    if my_sum + i == n:
        ans = i
        break
print(ans)