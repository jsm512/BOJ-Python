n=int(input())
arr=list(map(int,input().split()))
max_score=max(arr)
sum=0
for i in range(len(arr)):
    sum+=arr[i]/max_score*100
print(sum/n)