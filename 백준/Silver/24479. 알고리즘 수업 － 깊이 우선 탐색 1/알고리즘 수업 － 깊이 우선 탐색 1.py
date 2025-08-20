import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(graph, v , visted):
    global cnt 
    visted[v] = True
    count[v-1] = cnt
    cnt += 1

    for i in graph[v]:
        if not visted[i]:
            dfs(graph,i,visted)

n,m,r = map(int,input().split())
graph = []
for j in range(n+1):
    graph.append([])

for i in range(m):
    p,q = map(int,input().split())
    graph[p].append(q)
    graph[q].append(p)

visted = [False] * (n+1)
count = [0] * n
cnt = 1 

for i in (graph):
    i.sort()
dfs(graph,r,visted)

for i in (count):
    print(i)