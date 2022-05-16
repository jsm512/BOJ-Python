n = int(input())
input_time = list(map(int,input().split()))

input_time.sort()

min_time = 0

for i in range(n):
    for j in range(i+1):
        min_time += input_time[j]

print(min_time)
