n,m = map(int,input().split())
arr = list(map(int,input().split()))
max_sum = 0
my_sum = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            my_sum = arr[i]+arr[j]+arr[k]
            if (max_sum < my_sum) and (my_sum <= m):
                max_sum = my_sum
print(max_sum) 