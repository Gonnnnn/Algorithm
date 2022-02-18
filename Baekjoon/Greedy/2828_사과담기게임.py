N, M = map(int, input().split())
J = int(input())
apples = [int(input()) for _ in range(J)]

start = 1
end = M
result = 0
for apple in apples:
  to_move = 0
  if apple < start:
    to_move = apple - start
  elif end < apple:
    to_move = apple - end
  
  start += to_move
  end += to_move
  result += abs(to_move)

print(result)