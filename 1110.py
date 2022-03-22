n=int(input())
sum=n
cnt=0
while True:
    sum=(sum%10)*10+((sum//10)+(sum%10))%10
    cnt+=1
    if(sum==n):
        break
print(cnt)