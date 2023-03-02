from collections import deque
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            for j in range(4):
                nx = x + dx[i]
                ny = y + dy[j]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if arr[nx][ny] == 0:
                    continue
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    queue.append((nx,ny))
                    
while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0 :
        break
    arr = []
    for i in range(m):
        arr.append(list(map(int,input().split())))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    cnt = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                bfs(i,j)
                arr[i][j] = 0
                cnt+=1
    print(cnt)