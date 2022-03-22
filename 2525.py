a,b=map(int,input().split())
c=int(input())

if (b+c<60):
    print(a,b+c)
else:
    print((a+(b+c)//60)%24,(b+c)%60)

