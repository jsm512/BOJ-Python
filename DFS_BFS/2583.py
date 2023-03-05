from collections import deque


def bfs(x,y):
    queu = deque()
    queu.append((x,y))
    arr[x][y] = 1
    cnt = 1
    while queu:
        x,y = queu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                queu.append((nx,ny))
                cnt += 1
    ans.append(cnt)

m,n,k = map(int,input().split())
arr = [[0]*n for _ in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(k):
    start_x,start_y,end_x,end_y = map(int,input().split())
    for i in range(start_y,end_y):
        for j in range(start_x,end_x):
            arr[i][j] = 1
            
ans = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            bfs(i,j)
print(len(ans))
ans.sort()
for i in ans:
    print(i,end=' ')