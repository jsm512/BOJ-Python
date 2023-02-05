T = int(input())
for _ in range(T):
    d = int(input())
    for i in range(10001):
        if i + i**2 > d:
            print(i-1)
            break