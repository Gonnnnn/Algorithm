import sys
import heapq

input = sys.stdin.readline
N = int(input())
pq = [(lambda x: (x[0], -1 * (x[1] - x[0] + 1)))(list(map(int, input().split(' ')))) for _ in range(N)]
remains = []
heapq.heapify(pq)

height = [0 for _ in range(365 + 1)]
while(pq):
    row = [False for _ in range(365 + 1)]
    for _ in range(len(pq)):
        day, length = heapq.heappop(pq)
        if row[day]:
            remains.append((day, length))
            continue
        for i in range(length * -1):
            row[day + i] = True
            height[day + i] += 1
    pq = remains
    remains = []
answer = 0
Max = 0
length = 0
height.append(0)
for h in height:
    if h == 0:
        answer += length * Max
        Max, length = 0, 0
        continue
    Max = max(Max, h)
    length += 1
print(answer)