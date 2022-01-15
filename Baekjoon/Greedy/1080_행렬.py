# 문제
# 0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

# 행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)

# 입력
# 첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.

# 출력
# 첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.

import sys

n, m = map(int, input().split())

a = [list(map(int, input().strip())) for _ in range(n)]

b = [list(map(int, input().strip())) for _ in range(n)]

def check(array1, array2, x, y):
  for k in range(2):
    if((array1[y][x+k] == array2[y][x+k]) ^ (array1[y][x+1+k] == array2[y][x+1+k])):
      return False
  return True

def change(array1, array2, x, y):
  for p in range(3):
        for q in range(3):
            a[y+p][x+q] = 1 - a[y+p][x+q]

count = 0
possible = True
for j in range(0, n - 2):

  if(not possible):
    break
  
  for i in range(0, m - 2):
    if(i == m - 3):
      possible = check(a, b, i, j)
    
    if(a[j][i] != b[j][i]):
      count += 1
      change(a, b, i, j)

if(not possible or (a[n-2:n][:m] != b[n-2:n][:m])):
  print(-1)
else:
  print(count)