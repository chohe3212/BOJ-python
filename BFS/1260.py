import sys
from collections import deque
N,M,V = map(int,sys.stdin.readline().split())

graph = {}

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    if a not in graph:
        graph[a] = list()
    if b not in graph:
        graph[b] = list()
    graph[a].append(b)
    graph[b].append(a)

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

def dfs(graph, start_node):
    visited = list()
    need_visit = list()
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            if node not in graph:
                return visited
            for item in graph[node]:
                need_visit.append(item)
    return visited

for key in graph:
    graph[key].sort(reverse=True)
for item in dfs(graph, V):
    print(item, end=' ')
print()

for key in graph:
    graph[key].sort()
for item in bfs(graph, V):
    print(item, end=' ')
