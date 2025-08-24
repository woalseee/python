import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
from collections import deque

def bfs(graph, node, visited):
    global cnt
    queue = deque([node])
    visited[node] = True
    
    while queue:
        v = queue.popleft()
        count[v] = cnt
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n,m,r = map(int,input().split())
graph = []

for i in range(n+1):
    graph.append([])

for j in range(m):
    p,q = map(int,input().split())
    graph[p].append(q)
    graph[q].append(p)

visited = [False] * (n+1)
count = [0] * (n+1)
cnt = 1 

for i in (graph):
    i.sort()

bfs(graph,r,visited)

for i in range(1,n+1):
    print(count[i])