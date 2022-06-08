from ast import Num
from collections import deque


def bfs(x,y):
    global num
    num = 0
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx,ny))
                num+=1

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int,input())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0
check_num = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            bfs(i,j)
            arr[i][j] += cnt
            check_num.append(num)
            cnt+=1
print(cnt)
check_num.sort()
for x in check_num:
    if x == 0:
        x += 1
    print(x)