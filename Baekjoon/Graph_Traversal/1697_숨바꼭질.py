from collections import deque

# 수빈, 동생
N, K = map(int, input().split())


if N == K:
  print(0)
else:
  q = deque()
  q.append(N)
  sec = 0
  visited = [False]*100001
  while(q):
    sec += 1
    temp_len = len(q)
    for _ in range(temp_len):
      location = q.popleft()
      if location+1 == K or location-1 == K or location*2 == K:
        q = []
        break
      if location+1 <= 100000 and not visited[location+1]:
        q.append(location+1)
        visited[location+1] = True
      if 0 <= location-1 and not visited[location-1]:
        q.append(location-1)
        visited[location-1] = True
      if 2*location <= 100000 and not visited[location*2]:
        q.append(2*location)
        visited[location*2] = True
  
  print(sec)


## 애초에 table에 저장해나가는 방식
# from collections import deque
# MAX = 10 ** 5


# def bfs():
#     queue = deque([N])
#     while queue:
#         item = queue.popleft()
#         if item == K:
#             print(count[item])
#             break
#         for next_item in (item + 1, item - 1, item * 2):
#             if 0 <= next_item <= MAX and not count[next_item]:
#                 count[next_item] = count[item] + 1
#                 queue.append(next_item)


# N, K = map(int, input().split())
# count = [0] * (MAX + 1)
# bfs()