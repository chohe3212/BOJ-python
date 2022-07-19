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


T = int(sys.stdin.readline())
for _ in range(T):
    cnt=0
    N,M,K = map(int,sys.stdin.readline().split())
    graph = [[0]*M for _ in range(N)] # 기로M 세로 N에 맞는 이중 리스트 선언
    for i in range(K):
        X,Y = map(int,sys.stdin.readline().split())
        graph[X][Y] = 1

    for a in range(N):
        for b in range(M):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)
