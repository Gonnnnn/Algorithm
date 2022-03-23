# https://www.acmicpc.net/source/40713221
# 108ms이다. 함수화해보자 나도 나중에

import sys
input = sys.stdin.readline

gears = [[0]]
gears += [list(map(int, list(input().strip()))) for _ in range(4)]
K = int(input())

result = 0
# 각 기어 list에서 접점에 해당하는 부분의 idx
contact_idx = [6, 2, 6, 2, 6, 2, 6, 2]
for _ in range(K):
  # dir: 1시계 -1반시계
  gear_to_move, dir = map(int, input().split())

  # 접점에서 같은 극인지 확인
  same_pole_or_not = [True]
  same_pole_or_not += [True if gears[i][contact_idx[2*i-1]] != gears[i+1][contact_idx[2*i]] else False for i in range(1, len(gears)-1)]

  # 돌리는 방향 설정
  dirs = [0]*(len(gears))
  dirs[gear_to_move] = dir
  for i in range(gear_to_move-1, 0, -1):
    if same_pole_or_not[i]:
      dirs[i] = dirs[i+1] * -1
  for i in range(gear_to_move+1, len(gears)):
    if same_pole_or_not[i-1]:
      dirs[i] = dirs[i-1] * -1

  # idx 업데이트
  for i in range(1, len(dirs)):
    contact_idx[2*i-2] = (contact_idx[2*i-2] - dirs[i] + 8) % 8
    contact_idx[2*i-1] = (contact_idx[2*i-1] - dirs[i] + 8) % 8

for i in range(1, len(gears)):
  result += gears[i][contact_idx[2*i - 1]-2] * 2**(i-1)
print(result)