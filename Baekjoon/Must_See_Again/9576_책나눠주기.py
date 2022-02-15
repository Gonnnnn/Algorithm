# 문제
# 백준이는 방 청소를 하면서 필요 없는 전공 서적을 사람들에게 나눠주려고 한다. 나눠줄 책을 모아보니 총 N권이었다. 책이 너무 많기 때문에 백준이는 책을 구분하기 위해 각각 1부터 N까지의 정수 번호를 중복되지 않게 매겨 두었다.

# 조사를 해 보니 책을 원하는 서강대학교 학부생이 총 M명이었다. 백준이는 이 M명에게 신청서에 두 정수 a, b (1 ≤ a ≤ b ≤ N)를 적어 내라고 했다. 그러면 백준이는 책 번호가 a 이상 b 이하인 책 중 남아있는 책 한 권을 골라 그 학생에게 준다. 만약 a번부터 b번까지의 모든 책을 이미 다른 학생에게 주고 없다면 그 학생에게는 책을 주지 않는다.

# 백준이가 책을 줄 수 있는 최대 학생 수를 구하시오.

# 입력
# 첫째 줄에 테스트 케이스의 수가 주어진다.

# 각 케이스의 첫 줄에 정수 N(1 ≤ N ≤ 1,000)과 M(1 ≤ M ≤ 1,000)이 주어진다. 다음 줄부터 M개의 줄에는 각각 정수 ai, bi가 주어진다. (1 ≤ ai ≤ bi ≤ N)

# 출력
# 각 테스트 케이스마다 백준이가 책을 줄 수 있는 최대 학생 수를 한 줄에 하나씩 출력한다.

#이분 매칭 알고리즘을 이해하고 적용해봤으나 50~75%쯤에서 틀림

#import sys
#input = sys.stdin.readline

#def dfs(person):
#  for request in cases[person]:
#    if checked[request]:
#      continue
#    checked[request] = True
#    if books[request] == 0 or dfs(books[request]):
#      books[request] = person
#      return True
#  return False

#T = int(input())
#for _ in range(T):
#  N, M = map(int, input().split())
#  cases = [[0, 0]]
#  cases += [list(map(int, input().split())) for _ in range(M)]
#  books = [0]*(N+1)

#  result = 0
#  for i in range(1, len(cases)):
#    checked = [False]*(N+1)
#    if dfs(i):
#      result += 1

#  print(result)

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  req = [list(map(int, input().split())) for _ in range(M)]
  req.sort(key=lambda x:x[1])

  cnt = 0
  visited = [False]*(N+1)
  for a, b in req:
    for i in range(a, b+1):
      if not visited[i]:
        visited[i] = True
        cnt += 1
        break

  print(cnt)