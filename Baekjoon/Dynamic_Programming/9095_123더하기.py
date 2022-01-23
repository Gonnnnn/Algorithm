# 문제
# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

# 출력
# 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

T = int(input())
nums = [int(input()) for _ in range(T)]

def calc(n, table):
  if(n <= 2):
    return n
  elif(n == 3):
    return 4
  if(table[n] == 0):
    table[n] = calc(n-1, table) + calc(n-2, table) + calc(n-3, table)
    return table[n]
  return table[n]

for i in range(T):
  DP = [0]*(nums[i]+1)  
  print(calc(nums[i], DP))
