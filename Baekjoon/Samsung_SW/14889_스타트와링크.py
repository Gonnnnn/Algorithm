# not the best
# 그냥 combinations에서 N//2개 뽑아서 전부 비교해도 시간 덜 걸릴듯..

from itertools import combinations
N = int(input())
Table = [list(map(int, input().split())) for _ in range(N)]

def calc(arr):
  global N
  result = 0
  for case1, case2 in combinations(arr, 2):
    result += Table[case1][case2] + Table[case2][case1]
  return result

result = 1000
def solve(arr, idx):
  global N, result
  if len(arr) == N//2:
    Sum1 = calc(arr)
    another_arr = []
    for i in range(N):
      if i not in arr:
        another_arr.append(i)
    Sum2 = calc(another_arr)
    result = min(result, abs(Sum1-Sum2))
    return
    
  for i in range(idx+1, N):
    temp = arr[:]
    temp.append(i)
    solve(temp, i)
  return

solve([0], 0)
print(result)