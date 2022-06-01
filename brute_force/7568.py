n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

grade=[1 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            grade[j]+=1
for x in grade:
    print(x,end=' ')