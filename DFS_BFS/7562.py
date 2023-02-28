from collections import deque

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    while queue:
        a,b = queue.popleft()
        if a == a_x and b == a_y:
            return print(arr[a_x][a_y])
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < m and 0 <= ny < m and arr[nx][ny] == 0:
                queue.append((nx,ny))
                arr[nx][ny] = arr[a][b] + 1
for _ in range(int(input())):
    m = int(input())
    arr = [[0 for _ in range(m)] for _ in range(m)]
    x,y = map(int,input().split())
    a_x,a_y = map(int,input().split())
    dx = [-2,-2,-1,-1,1,1,2,2]
    dy = [1,-1,2,-2,2,-2,1,-1]
    bfs(x,y)
    