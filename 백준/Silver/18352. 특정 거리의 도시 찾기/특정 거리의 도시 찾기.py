import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph, node, visited, distance):
    queue = deque([node]) 
    visited[node] = True
    distance[node] = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[v] + 1

n,m,k,x = map(int,input().split())
graph = []  

for i in range(0,n+1):
    graph.append([])

for j in range(m):
    p,q = map(int,input().split())
    graph[p].append(q)
    
for s in (graph):
    s.sort()

visited = [False] * (n+1)
distance = [-1]*(n+1)

bfs(graph, x, visited, distance)

result = [i for i in range(1, n+1) if distance[i] == k]
if result:
    for r in result:
        print(r)
else:
    print(-1)