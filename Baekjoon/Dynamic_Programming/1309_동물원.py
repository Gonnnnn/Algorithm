N = int(input())

DP = [[0]*3 for _ in range(N+1)]
for i in range(3):
  DP[1][i] = 1

for i in range(2, N+1):
  DP[i][0] = (DP[i-1][0] + DP[i-1][1] + DP[i-1][2])%9901
  DP[i][1] = (DP[i-1][0] + DP[i-1][2])%9901
  DP[i][2] = (DP[i-1][0] + DP[i-1][1])%9901

print(sum(DP[N])%9901)

# 이것도 맞는데 시간 복잡도가 O(N^2) 허엉
# 진작에 생각했어야했는데
# 그래도 좋은 2차원 DP 연습
# if N == 1:
#   print(3)
# else:
#   DP = [[0] * (N+1) for _ in range(3)]
#   # DP 구조
#   # 첫 번째 열 : idx=0. N%3 == 0 에 해당하는 row
#   # 두 번째 열 : idx=1. N%3 == 1 에 해당하는 row
#   # 세 번째 열 : idx=2. N%3 == 2 에 해당하는 row
#   # 제일 아래의 반복문에서 위 3개 row를 순환하며 update해 나간다.
  
#   # 기본 세팅
#   for i in range(1, 3):
#     for j in range(3):
#       if j == 0:
#         DP[i][j] = 1
#       if j == 1:
#         DP[i][j] = i * 2
#       if i == j:
#         DP[i][j] = 2

#   for i in range(3, N+1):
#     idx = i%3
#     for j in range(N+1):
#       if j == 0:
#         DP[idx][j] = 1
#       elif j == 1:
#         DP[idx][j] = i*2
#       elif 1 < j < i:
#         DP[idx][j] = (DP[idx-1][j] + DP[idx-1][j-1] + DP[idx-2][j-1]) % 9901
        
#       # i==j인 경우 경우의 수는 2개
#       # 더 이상 진행할 필요 없으므로 break
#       if i == j:
#         DP[idx][j] = 2
#         break

#   print(sum(DP[N%3]))