N, K = map(int, input().split())
table = list(input())

result = 0
for i in range(N):
  if table[i] == 'P':
    start = i-K
    end = i+K+1
    if i <= K:
      start = 0
    if i >= N-K-1:
      end = N
    for j in range(start, end):
      if j == i:
        continue
      if table[j] == 'H':
        table[j] = 'X'
        result += 1
        break

print(result)