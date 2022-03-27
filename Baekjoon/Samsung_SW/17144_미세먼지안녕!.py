// 지금 코드 정리할 시간이 딱히 없다. 다음에 하자. 정리할건 많이 있네.

import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
Map = []
cleaner = []
for i in range(R):
  temp = list(map(int, input().split()))
  if temp[0] == -1:
    cleaner.append(i)
  Map.append(temp)

def defuse(y, x, Map_for_calc):
  global R, C
  dy = [1, 0, -1, 0]
  dx = [0, 1, 0, -1]

  defused_dust = Map[y][x] // 5
  count = 0
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if 0 <= ny < R and 0 <= nx < C:
      if Map[ny][nx] != -1:
        Map_for_calc[ny][nx] += defused_dust
        count += 1
  Map_for_calc[y][x] -= defused_dust * count
  return

def update(Map_for_calc):
  global R, C
  
  for i in range(R):
    for j in range(C):
      Map[i][j] += Map_for_calc[i][j]
  return
  

def circulate():
  top = cleaner[0]
  bottom = cleaner[1]
  
  to_put = 0
  # top : counter clockwise circulation
  for i in range(1, C):
    temp = Map[top][i]
    Map[top][i] = to_put
    to_put = temp
  for i in range(top-1, -1, -1):
    temp = Map[i][-1]
    Map[i][-1] = to_put
    to_put = temp
  for i in range(C-2, -1, -1):
    temp = Map[0][i]
    Map[0][i] = to_put
    to_put = temp
  for i in range(1, top):
    temp = Map[i][0]
    Map[i][0] = to_put
    to_put = temp

  # bottom : clockwise circulation
  to_put = 0
  for i in range(1, C):
    temp = Map[bottom][i]
    Map[bottom][i] = to_put
    to_put = temp
  for i in range(bottom+1, R):
    temp = Map[i][-1]
    Map[i][-1] = to_put
    to_put = temp
  for i in range(C-2, -1, -1):
    temp = Map[-1][i]
    Map[-1][i] = to_put
    to_put = temp
  for i in range(R-2, bottom, -1):
    temp = Map[i][0]
    Map[i][0] = to_put
    to_put = temp
  return

for _ in range(T):
  Map_for_calc = [[0]*C for _ in range(R)]
  for i in range(R):
    for j in range(C):
      if j == 0 and (i == cleaner[0] or i == cleaner[1]):
        continue
      else:
        defuse(i, j, Map_for_calc)
  update(Map_for_calc)
  circulate()

result = 2
for i in range(R):
  for j in range(C):
    result += Map[i][j]

print(result)