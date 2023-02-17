a,b = input().split()

ans = 0
ans_arr = []

if len(b) - len(a) == 0:
    for i in range(len(a)):
        if a[i] != b[i]:
            ans += 1
    print(ans)     
else:
    for i in range(len(b)-len(a)+1):
        num = 0
        for j in range(len(a)):
            if a[j] != b[i+j]:
                num += 1
        ans_arr.append(num)
    print(min(ans_arr))