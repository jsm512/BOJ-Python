from collections import deque
import sys

m,n = map(int,sys.stdin.readline().split())
tomato=[]
for _ in range(n):
    tomato.append(list(map(int,sys.stdin.readline().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

start_tomato = []
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            start_tomato.append([i,j])

def bfs(start_tomato):
    q = deque()
    for i in start_tomato:
        q.append(i)
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tomato[nx][ny] == -1:
                continue
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                q.append((nx,ny))

bfs(start_tomato)

ans = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit(0)
        ans = max(ans,tomato[i][j])
print(ans-1)