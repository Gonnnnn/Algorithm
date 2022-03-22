import sys
input = sys.stdin.readline

N, L = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

def solve(line):
  global N, L
  cells = []
  temp = -1
  count = 0
  for i in range(N):
    if temp == line[i]:
      cells[-1][1] += 1
    else:
      temp = line[i]
      count = 1
      cells.append([temp, count])

  for i in range(1, len(cells)):
    cur = cells[i]
    prev = cells[i-1]
    if abs(cur[0] - prev[0]) > 1:
      return False
    
    if prev[0] < cur[0]:
      if prev[1] < L:
        return False
    else:
      if cur[1] < L:
        return False
      else:
        cur[1] -= L
  
  return True

result = 0
for i in range(N):
  if solve(Map[i][:]):
    result += 1
  col = []
  for j in range(N):
    col.append(Map[j][i])
  if solve(col):
    result += 1

print(result)