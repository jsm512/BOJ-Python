from collections import deque


def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if cabbage[nx][ny] == 0:
                continue
            if cabbage[nx][ny] == 1:
                cabbage[nx][ny] = 0
                queue.append((nx,ny))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(int(input())):
    m,n,k=map(int,input().split())
    cabbage=[[0]*n for _ in range(m)]
    for _ in range(k):
        a,b = map(int,input().split())
        cabbage[a][b] += 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if cabbage[i][j] == 1:
                bfs(i,j)
                cabbage[i][j] = 0
                cnt+=1
    print(cnt)

