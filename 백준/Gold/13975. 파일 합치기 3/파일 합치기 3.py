import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    pages = list(map(int, input().split(' ')))
    heapq.heapify(pages)
    total = 0
    while(len(pages) >= 2):
        f1 = heapq.heappop(pages)
        f2 = heapq.heappop(pages)
        total += f1 + f2
        heapq.heappush(pages,f1 + f2)
    print(total)