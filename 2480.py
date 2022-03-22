abc=list(map(int,input().split()))

if (len(set(abc))==1):
    print(10000+abc[0]*1000)
elif (len(set(abc))==2):
    for i in range(len(abc)):
        cnt=abc.count(abc[i])
        if(cnt==2):
            print(1000+abc[i]*100)
            break
else:
    print(max(abc)*100)
