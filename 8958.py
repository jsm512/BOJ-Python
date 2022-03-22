T=int(input())
for i in range(T):
    arr=list(input().strip())
    sum=0
    cnt=0
    for j in arr:
        if(j=='O'):
            cnt+=1
            sum+=cnt
        else:
            cnt=0
    print(sum)