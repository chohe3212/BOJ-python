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

N,M = map(int,sys.stdin.readline().split())

cnt = 0
result_list=[[0]*M for _ in range(N)]
for i in range(N):
    list1 = list(map(int,sys.stdin.readline().split()))
    for j in range(M):
        sum = list1[j*3]+list1[j*3+1]+list1[j*3+2]
        avg = sum / 3
        result_list[i][j]=avg

final_list = [[0]*M for _ in range(N)]

T = int(sys.stdin.readline())
for i in range(N):
    for j in range(M):
        if result_list[i][j] >= T:
            final_list[i][j] = 1
for a in range(N):
    for b in range(M):
        if final_list[a][b] == 1:
            bfs (final_list,a,b)
            cnt +=1
print(cnt)
