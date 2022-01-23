# 문제
# 수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

# 김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

# 참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

# 수강신청 대충한 게 찔리면, 선생님을 도와드리자!

# 입력
# 첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

# 이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)

# 출력
# 강의실의 개수를 출력하라.

import sys
import heapq
input = sys.stdin.readline

N = int(input())
lectures = []
for _ in range(N):
  start, end = map(int, input().split())
  lectures.append((start, end))
lectures.sort()

rooms = []
heapq.heappush(rooms, lectures[0][1])
for i in range(1, N):
  if(lectures[i][0] >= rooms[0]):
    # 교체
    heapq.heappop(rooms)
    heapq.heappush(rooms, lectures[i][1])
  else:
    # 추가
    heapq.heappush(rooms, lectures[i][1])

print(len(rooms))

# 처음에 떠올린 방법. 틀린건 아니다. 다만 시간 초과. 훨씬 더 효율적인 방법이 있는 것
# import sys
# import heapq
# input = sys.stdin.readline

# N = int(input())
# lectures = []
# for _ in range(N):
#   start, end = map(int, input().split())
#   heapq.heappush(lectures, (end, start))

# count = 0

# while(len(lectures) != 0):
#   temp = heapq.heappop(lectures)
#   temp_lectures = []
#   while(len(lectures) != 0):
#     lecture = heapq.heappop(lectures)
#     if temp[0] > lecture[1]:
#       heapq.heappush(temp_lectures, lecture)
#     else:
#       temp = lecture
#   count += 1
#   lectures = temp_lectures
# print(count)