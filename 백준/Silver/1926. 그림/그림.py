import sys
from collections import deque


input = sys.stdin.readline
n, m = map(int, input().split(' '))
drawings = [list(map(int, input().split(' '))) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1 ,0]
def bfs(sy, sx):
    global n, m
    q = deque([[sy, sx]])
    drawings[sy][sx] = 0
    size = 0
    while(q):
        y, x = q.popleft()
        size += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or n <= ny: continue
            if nx < 0 or m <= nx: continue
            if drawings[ny][nx] == 0: continue
            drawings[ny][nx] = 0
            q.append([ny, nx])
    return size

num = 0
maxSize = 0
for i in range(n):
    for j in range(m):
        if drawings[i][j] == 0: continue
        size = bfs(i, j)
        maxSize = max(size, maxSize)
        if size: num += 1
print(num)
print(maxSize)