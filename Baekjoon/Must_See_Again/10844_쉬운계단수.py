# 문제
# 45656이란 수를 보자.

# 이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

# 입력
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

N = int(input())

DP = [[0, 0]]
for i in range(9):
  DP.append([1, 0])

switch = 0
for i in range(1, N):
  switch += 1
  new = switch % 2
  old = (switch + 1) % 2
  for j in range(0, 10):
    if j == 0:
      DP[j][new] = DP[1][old]
    elif j == 9:
      DP[j][new] = DP[8][old]
    else:
      DP[j][new] = DP[j-1][old] + DP[j+1][old]

result = 0
for i in range(len(DP)):
  result += DP[i][switch % 2]
print(result%1000000000)