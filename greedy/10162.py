arr = [300,60,10] #A,B,C의 버튼(초단위)
T = int(input()) #초단위
ans = []
if T % 10 != 0:
    print(-1)
else:
    while True:
        if T == 0:
            break
        for i in arr:
            ans.append(T // i)
            T = T % i
    for i in ans:
        print(i, end=' ')