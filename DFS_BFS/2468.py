from collections import deque


def bfs(x,y,safe,check_rain):
    queue = deque()
    queue.append((x,y))

    check_rain[x][y] = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if rain[nx][ny] > safe and check_rain[nx][ny] == 0:
                check_rain[nx][ny] = 1
                queue.append((nx,ny))

n = int(input())

rain = []
for i in range(n):
    rain.append(list(map(int,input().split())))
    max_rain = max(rain[i])
    if max_rain < max(rain[i]):
        max_rain = max(rain[i])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

max_result = 0
for i in range(max_rain):
    check_rain = [[0] * n for i in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if rain[j][k] > i and check_rain[j][k] == 0:
                bfs(j,k,i,check_rain)
                cnt+=1
    if max_result < cnt:
        max_result = cnt
print(max_result)
