# https://www.acmicpc.net/source/40822187
# 내꺼보다 한 3배는 빠르다

import copy

# row, col
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

def up(y, x, temp_Map):
  global N, M
  for i in range(y-1, -1, -1):
    if temp_Map[i][x] == 6:
      break
    elif temp_Map[i][x] == 0:
      temp_Map[i][x] = -1
  return

def down(y, x, temp_Map):
  global N, M
  for i in range(y+1, N):
    if temp_Map[i][x] == 6:
      break
    elif temp_Map[i][x] == 0:
      temp_Map[i][x] = -1
  return
  
def right(y, x, temp_Map):
  global N, M
  for i in range(x+1, M):
    if temp_Map[y][i] == 6:
      break
    elif temp_Map[y][i] == 0:
      temp_Map[y][i] = -1
  return

def left(y, x, temp_Map):
  global N, M
  for i in range(x-1, -1, -1):
    if temp_Map[y][i] == 6:
      break
    elif temp_Map[y][i] == 0:
      temp_Map[y][i] = -1
  return

def cctv1(dir, y, x, temp_Map):
  global N, M
  if dir == 0:
    right(y, x, temp_Map)
  elif dir == 1:
    down(y, x, temp_Map)
  elif dir == 2:
    left(y, x, temp_Map)
  else:
    up(y, x, temp_Map)
  return

def cctv2(dir, y, x, temp_Map):
  global N, M
  if dir == 0:
    left(y, x, temp_Map)
    right(y, x, temp_Map)
  else:
    up(y, x, temp_Map)
    down(y, x, temp_Map)
  return

def cctv3(dir, y, x, temp_Map):
  global N, M
  if dir == 0:
    up(y, x, temp_Map)
    right(y, x, temp_Map)
  elif dir == 1:
    right(y, x, temp_Map)
    down(y, x, temp_Map)
  elif dir == 2:
    down(y, x, temp_Map)
    left(y, x, temp_Map)
  else:
    left(y, x, temp_Map)
    up(y, x, temp_Map)
  return

def cctv4(dir, y, x, temp_Map):
  if dir == 0:
    left(y, x, temp_Map)
    up(y, x, temp_Map)
    right(y, x, temp_Map)
  elif dir == 1:
    up(y, x, temp_Map)
    right(y, x, temp_Map)
    down(y, x, temp_Map)
  elif dir == 2:
    right(y, x, temp_Map)
    down(y, x, temp_Map)
    left(y, x, temp_Map)
  else:
    down(y, x, temp_Map)
    left(y, x, temp_Map)
    up(y, x, temp_Map)
  return
    
def cctv5(dir, y, x, temp_Map):
  up(y, x, temp_Map)
  right(y, x, temp_Map)
  down(y, x, temp_Map)
  left(y, x, temp_Map)
  return

cctvs = []
for i in range(N):
  for j in range(M):
    if 1<=Map[i][j]<=5:
      cctvs.append([Map[i][j], i, j])

# cctv종류:다른방향을보는 최소 회전 횟수
# 1:4, 2:2, 3:4, 4:4, 5:1
cctv_rotate = [0, 4, 2, 4, 4, 1]
result = N*M
def solve(cctv_idx, Map):
  global N, M, result
  if cctv_idx == len(cctvs):
    count = 0
    for i in range(N):
      for j in range(M):
        if Map[i][j] == 0:
          count += 1
    result = min(result, count)
    return result

  cctv = cctvs[cctv_idx]
  iteration = cctv_rotate[cctv[0]]
  temp = N*M
  if cctv[0] == 1:
    for i in range(iteration):
      Map_copy = copy.deepcopy(Map)
      cctv1(i, cctv[1], cctv[2], Map_copy)
      temp = min(temp, solve(cctv_idx+1, Map_copy))
  elif cctv[0] == 2:
    for i in range(iteration):
      Map_copy = copy.deepcopy(Map)
      cctv2(i, cctv[1], cctv[2], Map_copy)
      temp = min(temp, solve(cctv_idx+1, Map_copy))
  elif cctv[0] == 3:
    for i in range(iteration):
      Map_copy = copy.deepcopy(Map)
      cctv3(i, cctv[1], cctv[2], Map_copy)
      temp = min(temp, solve(cctv_idx+1, Map_copy))
  elif cctv[0] == 4:
    for i in range(iteration):
      Map_copy = copy.deepcopy(Map)
      cctv4(i, cctv[1], cctv[2], Map_copy)
      temp = min(temp, solve(cctv_idx+1, Map_copy))
  elif cctv[0] == 5:
    for i in range(iteration):
      Map_copy = copy.deepcopy(Map)
      cctv5(i, cctv[1], cctv[2], Map_copy)
      temp = min(temp, solve(cctv_idx+1, Map_copy))

  return temp

print(solve(0, Map))