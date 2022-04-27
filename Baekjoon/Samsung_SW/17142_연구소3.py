import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
viruses = []
Map = []
for i in range(N):
  row = list(map(int, input().split()))
  for j in range(N):
    if row[j] == 2:
      viruses.append([i, j])
  Map.append(row)

def checkZero(temp_Map):
  global N
  for i in range(N):
    for j in range(N):
      if temp_Map[i][j] == 0:
        return True
  return False

result = sys.maxsize
for actives in combinations(viruses, M):
  temp_Map = copy.deepcopy(Map)
  time = 0
  for y, x in actives:
    temp_Map[y][x] = 3

  q = deque(actives)
  dy = [-1, 0, 1, 0]
  dx = [0, -1, 0, 1]
  while(q):
    q_len = len(q)
    spread_out = False
    for _ in range(q_len):
      y, x = q.popleft()
      for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
          if temp_Map[ny][nx] == 0:
            temp_Map[ny][nx] = 3
            q.append([ny, nx])
            # we could say it spreads out only when it's copied to an empty cell
            # it doesnt count when it activates another inactive virus
            spread_out = True

          elif temp_Map[ny][nx] == 2:
            temp_Map[ny][nx] = 3
            q.append([ny, nx])

    if not spread_out:
      if not checkZero(temp_Map):
        break
    time += 1
      
  # check
  if checkZero(temp_Map):
    time = sys.maxsize

  # update the answer
  if time < result:
    result = time

if result == sys.maxsize:
  result = -1
print(result)