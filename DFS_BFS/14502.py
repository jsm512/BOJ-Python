from collections import deque
import sys


n,m=map(int,sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

virus=[]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            virus.append([i,j])
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    copy_arr=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            copy_arr[i][j] = arr[i][j]
    q = deque()
    for i in virus:
        q.append(i)
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if copy_arr[nx][ny] == 0:
                copy_arr[nx][ny] = 2
                q.append((nx,ny))
    global my_result
    cnt = 0
    for i in copy_arr:
        cnt += i.count(0)
    my_result = max(my_result,cnt)

def built_wall(num):
    if num == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                built_wall(num+1)
                arr[i][j] = 0
my_result = 0
built_wall(0)
print(my_result)