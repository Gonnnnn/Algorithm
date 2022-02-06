# 문제
#     +---+        
#     | D |        
# +---+---+---+---+
# | E | A | B | F |
# +---+---+---+---+
#     | C |        
#     +---+        
# 주사위는 위와 같이 생겼다. 주사위의 여섯 면에는 수가 쓰여 있다. 위의 전개도를 수가 밖으로 나오게 접는다.

# A, B, C, D, E, F에 쓰여 있는 수가 주어진다.

# 지민이는 현재 동일한 주사위를 N3개 가지고 있다. 이 주사위를 적절히 회전시키고 쌓아서, N×N×N크기의 정육면체를 만들려고 한다. 이 정육면체는 탁자위에 있으므로, 5개의 면만 보인다.

# N과 주사위에 쓰여 있는 수가 주어질 때, 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. 둘째 줄에 주사위에 쓰여 있는 수가 주어진다. 위의 그림에서 A, B, C, D, E, F에 쓰여 있는 수가 차례대로 주어진다. N은 1,000,000보다 작거나 같은 자연수이고, 쓰여 있는 수는 50보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 문제의 정답을 출력한다.

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

if N == 1:
  print(sum(numbers) - max(numbers))
else:
  MAX_ONE_SIDE = 50

  exception = []
  for i in range(6):
    exception.append([i, len(numbers)-1-i])

  one_side = min(numbers)

  two_side = MAX_ONE_SIDE * 2
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      if([i, j] in exception):
        continue
      if two_side > numbers[i] + numbers[j]:
        two_side = numbers[i] + numbers[j]

  three_side = MAX_ONE_SIDE * 3
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      for k in range(j + 1, len(numbers)):
        if([i, j] in exception or [i, k] in exception or [j, k] in exception):
          continue
        if three_side > numbers[i] + numbers[j] + numbers[k]:
          three_side = numbers[i] + numbers[j] + numbers[k]

  result = one_side * ((N-1)*(N-2)*4 + (N-2)*(N-2)) + two_side * ((N-1)*4 + (N-2)*4) + three_side * 4
  print(result)

# 위의 논리를 잘 생각해보면, 만날 수 없는 부분들(3부분)로 주사위의 면을 나눠서, 만날 수 없는 부분 중 하나씩, 총 3개를 골라 조합을 이루었을 때, 그 면들은 항상 주사위의 겉 부분에 나타내어질 수 있는 면들이다.

# 아래는 그 예시
# import sys

# input = sys.stdin.readline

# n = int(input())
# arr1 = list(map(int, input().split()))

# if n == 1:
#     print(sum(arr1) - max(arr1))
# else:
#     arr = [min(arr1[0], arr1[5]), min(arr1[1], arr1[4]), min(arr1[2], arr1[3])]
#     arr.sort()
#     res0 = (arr[0] + arr[1]) * (n - 1) * 4
#     res1 = (arr[0] + arr[1]) * (n - 2) * 4
#     res2 = (arr[0] + arr[1] + arr[2]) * 4
#     res3 = (arr[0]) * (n - 2) * 4
#     res4 = arr[0] * (n - 2) * (n - 2) * 5
#     print(res0+res1+res2+res3+res4)