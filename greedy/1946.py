import sys


t = int(input())

for i in range(t):
    n = int(input())
    arr = []
    cnt = 1
    for j in range(n):
        arr.append(list(map(int,sys.stdin.readline().split())))
    arr.sort()
    check = arr[0][1]

    for j in range(1,n):
        if check > arr[j][1]:
            cnt+=1
            check = arr[j][1]
    print(cnt)