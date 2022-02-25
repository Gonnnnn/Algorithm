# 원생, 조
N, K = map(int, input().split())
kids = list(map(int, input().split()))

height_difference = []
for i in range(N-1):
  height_difference.append(kids[i+1]-kids[i])
height_difference.sort(reverse=True)
print(sum(height_difference[K-1:]))