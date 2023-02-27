# def sel_sort(d):
#     n = len(d)
#     for i in range(0,n-1):
#         min_idx = i
#         for j in range(i,n):
#             if d[j] > d[min_idx]:
#                 min_idx = j
#         d[i],d[min_idx] = d[min_idx],d[i]
        
n = int(input())
arr = list(map(int,input().split()))
cnt = n+2
arr.sort(reverse=True)

for i in range(n):
    arr[i] = arr[i] - (n-i)
print(cnt+max(arr))