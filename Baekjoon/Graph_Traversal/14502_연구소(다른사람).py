# 기본적인 논리는 다 같다.
# 내꺼는 1328, 이 코드는 376ms가 걸렸다.
# 그 차이를 알아내고 싶다.

from collections import deque
import sys
from itertools import combinations

input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n, m = map(int, input().split())

def bfs(graph, viruses):
    q = deque(viruses)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx, ny))

def countZero(graph):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    return count

graph = []
zeros = []
viruses = []
for x in range(n):
    graph.append(list(map(int, input().split())))
    for y in range(m):
        if graph[x][y] == 0:
            zeros.append((x, y))
        elif graph[x][y] == 2:
            viruses.append((x, y))

combs = combinations(zeros, 3)
max_res = 0
for comb in combs:
    copy_graph = [i[:] for i in graph]
    for x, y in comb:
        copy_graph[x][y] = 1
    bfs(copy_graph, viruses)
    res = countZero(copy_graph)
    max_res = max(max_res, res)

print(max_res)