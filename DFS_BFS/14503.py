from collections import deque
import sys

def left():
    global d
    d -= 1
    if d == -1:
        d = 3

def bfs(x,y,cnt,turn_num):
    while True:
        left()
        nx = x + dx[d]
        ny = y + dy[d]

        if check[nx][ny] == 0 and arr[nx][ny] == 0:
            check[nx][ny] = 1
            cnt += 1
            x = nx
            y = ny
            turn_num = 0
        else:
            turn_num += 1
        if turn_num == 4:
            nx = x - dx[d]
            ny = y - dy[d]
            if arr[nx][ny] != 1:
                x = nx
                y = ny
                turn_num = 0
            else:
                break

    return cnt            




n,m=map(int,sys.stdin.readline().split())
r,c,d=map(int,sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
check=[[0]*m for _ in range(n)]
check[r][c] = 1
cnt = 1
turn_num = 0
dx=[-1,0,1,0]
dy=[0,1,0,-1]

print(bfs(r,c,cnt,turn_num))