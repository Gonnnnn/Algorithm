from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
operators_num = list(map(int, input().split()))

# + - * /
operators = []
for i, num in enumerate(operators_num):
  for _ in range(num):
    operators.append(i)

Min = 1000000000
Max = -1 * 1000000000
for case in permutations(operators, N-1):
  result = A[0]
  for idx, operator in enumerate(case):
    if operator == 0:
      result += A[idx + 1]
    elif operator == 1:
      result -= A[idx + 1]
    elif operator == 2:
      result *= A[idx + 1]
    else:
      if result < 0:
        result *= -1
        result = result // A[idx + 1]
        result *= -1
      else:
        result = result // A[idx + 1]
  Min = min(result, Min)
  Max = max(result, Max)

print(Max)
print(Min)