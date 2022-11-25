import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().strip().split(' '))
jewelries = [list(map(int, input().strip().split(' '))) for _ in range(N)]
bags = [int(input().strip()) for _ in range(K)]
jewelries.sort(reverse=True)
bags.sort()
jewelriesThatFitInTheCurrentBag = []

result = 0
for bag in bags:
    while(jewelries and jewelries[-1][0] <= bag):
        weight, value = jewelries.pop()
        heapq.heappush(jewelriesThatFitInTheCurrentBag, -1 * value)
    if jewelriesThatFitInTheCurrentBag:
        value = heapq.heappop(jewelriesThatFitInTheCurrentBag)
        result += value
print(-1 * result)