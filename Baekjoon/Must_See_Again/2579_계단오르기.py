# 문제
# 계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다. <그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.



# <그림 1>
# 시작, 10, 20, 15, 25, 10, 20(도착)

# 예를 들어 <그림 2>와 같이 시작점에서부터 첫 번째, 두 번째, 네 번째, 여섯 번째 계단을 밟아 도착점에 도달하면 총 점수는 10 + 20 + 25 + 20 = 75점이 된다.



# <그림 2>
# 시작->10->20->25->20(도착)

# 계단 오르는 데는 다음과 같은 규칙이 있다.

# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.
# 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.

# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 입력의 첫째 줄에 계단의 개수가 주어진다.

# 둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

# 출력
# 첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.

import sys
input = sys.stdin.readline

n = int(input())
steps = [10000]
for _ in range(n):
  steps.append(int(input()))
DP = [[0, 0] for _ in range(n+1)]
DP[1][0] = steps[1]

def calc(n):
  if(n <= 1):
    return DP[n]
  if(DP[n][0] == 0 and DP[n][1] == 0):
    one_before = calc(n-1)
    two_before = calc(n-2)
    DP[n][0] = max(two_before[0], two_before[1]) + steps[n]
    DP[n][1] = one_before[0] + steps[n]
  return DP[n]

result = calc(n)
print(max(result[0], result[1]))

# 다른 풀이. 이게 최적의 해를 주는 이유는 잘 모르겠다
# import sys

# n = int(sys.stdin.readline())
# score = [0] * 301
# for i in range(n):
#     score[i] = int(sys.stdin.readline())
# max_sum = [0] * 301

# max_sum[0] = score[0]
# max_sum[1] = score[0] + score[1]
# max_sum[2] = max(score[0]+score[2], score[1] + score[2])

# for i in range(3, n):
#     max_sum[i] = max(max_sum[i - 3] + score[i-1] + score[i], max_sum[i-2] + score[i])

# print(max_sum[n-1])