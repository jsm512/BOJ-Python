from collections import deque


def bfs(x,y):
    queu = deque()
    queu.append((x,y))
    arr[x][y] = 2 
    while queu:
        x,y = queu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == 1:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
                queu.append((nx,ny))
        
m,n = map(int,input().split())
arr = [list(map(int,list(input()))) for _ in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    if arr[0][i] == 0:
        bfs(0,i)
if 2 in arr[m-1]:
    print("YES")
else:
    print("NO")