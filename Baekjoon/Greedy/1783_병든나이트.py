# 세로, 가로
N, M = map(int, input().split())

result = 1
if N == 2:
  result += (min(M, 7)-1)//2
elif N >= 3:
  if M < 7:
    result += min(M, 4)-1
  else:
    result += M - 3
print(result)