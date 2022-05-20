import sys


n = int(input())

start_end = []
for i in range(n):
    start_end.append(list(map(int,sys.stdin.readline().split())))
start_end.sort(reverse=True)

check = start_end[0][0]
cnt = 1
for i in range(1,n):
    if check >= start_end[i][1]:
        cnt += 1
        check = start_end[i][0]

print(cnt)
        
