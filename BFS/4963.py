from collections import deque
import sys

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, a,b): # bfs로 a,b 에 근접한 값들을 0으로 바꿔줌! 
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

