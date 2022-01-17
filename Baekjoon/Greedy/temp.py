import heapq as hq

a = [[4,3], [1,4], [1,3]]
hq.heapify(a)

for i in range(len(a)):
  print(hq.heappop(a))