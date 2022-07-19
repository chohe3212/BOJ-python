import sys
from collections import deque

def bfs(graph, start_node):
    visited = list()
    need_visit = deque()
    
    need_visit.append(start_node)
    while need_visit: 
        node = need_visit.popleft() 
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
            if len(visited) == 2:
                return visited[1]
    return visited

graph = {}

N = int(sys.stdin.readline())
for _ in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    if a not in graph:
        graph[a] = list()
    if b not in graph:
        graph[b] = list()
    graph[a].append(b)
    graph[b].append(a)

for i in range(2,N+1):
    print(bfs(graph, i))
