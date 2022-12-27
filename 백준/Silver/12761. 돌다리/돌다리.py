import sys
from collections import deque

def getNextLocs(cur):
    global a, b, Max
    buffer = []
    if cur - 1 >= 0: buffer.append(cur - 1)
    if cur + 1 <= Max: buffer.append(cur + 1)
    if cur - a >= 0: buffer.append(cur - a)
    if cur + a <= Max: buffer.append(cur + a)
    if cur - b >= 0: buffer.append(cur - b)
    if cur + b <= Max: buffer.append(cur + b)
    if cur * a <= Max: buffer.append(cur * a)
    if cur * b <= Max: buffer.append(cur * b)
    return buffer

input = sys.stdin.readline
a, b, n, m = map(int, input().split(' '))
Max = 100_000

q = deque([n])
visited = [False for _ in range(Max + 1)]
cnt = 0
while(True):
    length = len(q)
    cur = -1
    for _ in range(length):
        cur = q.popleft()
        if cur == m: break
        nextLocs = getNextLocs(cur)
        for loc in nextLocs:
            if visited[loc]: continue
            visited[loc] = True
            q.append(loc)
    if cur == m: break
    cnt += 1
print(cnt)