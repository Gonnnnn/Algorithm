N, M = map(int, input().split())
books = list(map(int, input().split()))
books.sort()
idx = N
for i in range(N):
  if books[i] > 0:
    idx = i
    break

result = 0
for i in range(0, idx//M):
  result += abs(books[i*M]) * 2

if idx%M != 0:
  result += abs(books[idx-idx%M]) * 2

for i in range(0, (N-idx)//M):
  result += books[(N-1)-(i*M)] * 2

if (N-idx)%M != 0:
  result += books[idx+(N-idx)%M - 1] * 2

if abs(books[0]) >= abs(books[-1]):
  result -= abs(books[0])
else:
  result -= abs(books[-1])

print(result)