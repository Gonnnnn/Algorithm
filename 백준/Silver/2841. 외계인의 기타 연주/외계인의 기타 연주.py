import sys
import heapq

input = sys.stdin.readline
# 음의 개수, 프렛 수
N, P = map(int, input().split(' '))
pqs = [[] for _ in range(N + 1)]
answer = 0
for _ in range(N):
    stringNum, fret = map(int, input().split(' '))
    while(pqs[stringNum]):
        peek = pqs[stringNum][0] * -1
        if peek <= fret: break
        heapq.heappop(pqs[stringNum])
        answer += 1
    if pqs[stringNum] and pqs[stringNum][0] * -1 == fret: continue
    heapq.heappush(pqs[stringNum], fret * -1)
    answer += 1
print(answer)