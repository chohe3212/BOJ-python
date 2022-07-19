from collections import deque

def bfs(graph, start_node):
    visited = list()
    need_visit = deque()
    
    need_visit.append(start_node)
    while need_visit: 
        node = need_visit.popleft() 
        if node not in visited: 
            visited.append(node)
            if node not in graph:
                return visited
            for item in graph[node]:
                need_visit.append(item)
            
    return visited

N = int(input())
M = int(input())

graph = {}
for _ in range(M):
    a,b = map(int,input().split())
    if a not in graph:
        graph[a] = list()
    if b not in graph:
        graph[b] = list()
    graph[a].append(b)
    graph[b].append(a)

print(len(bfs(graph,1))-1) # 1번 컴퓨터는 빼준다