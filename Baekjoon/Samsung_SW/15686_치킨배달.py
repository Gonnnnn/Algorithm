import sys
from itertools import combinations

input = sys.stdin.readline
# N:가로세로, M:폐업 후 남겨지는 치킨집 개수
N, M = map(int, input().split())
Map = []
chickens = []
houses = []
for i in range(N):
  row = list(map(int, input().split()))
  Map.append(row)
  for j in range(N):
    if row[j] == 2:
      chickens.append([i, j])
    elif row[j] == 1:
      houses.append([i, j])

result = float('inf')
for case in combinations(chickens, M):
  temp_result = 0
  for house_y, house_x in houses:
    temp = float('inf')
    for y, x in case:
      temp = min(temp, abs(house_y-y) + abs(house_x-x))
    temp_result += temp
  result = min(result, temp_result)
print(result)    