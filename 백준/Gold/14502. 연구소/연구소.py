from itertools import combinations
from collections import deque

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

empty_spaces = []
virus_positions = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            empty_spaces.append((i,j))
        elif arr[i][j] == 2:
            virus_positions.append((i,j))

def bfs(lab_copy):
    queue = deque(virus_positions)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and lab_copy[nx][ny] == 0:
                lab_copy[nx][ny] = 2
                queue.append((nx, ny))
    safe_area = 0
    for i in range(n):
        safe_area += lab_copy[i].count(0)
    return safe_area

max_safe = 0
for walls in combinations(empty_spaces, 3):
    lab_copy = [row[:] for row in arr]
    for x, y in walls:
        lab_copy[x][y] = 1
    safe = bfs(lab_copy)
    if safe > max_safe:
        max_safe = safe

print(max_safe)
